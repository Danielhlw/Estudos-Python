# Documentação Técnica: Kafka, MongoDB, CDC e Conectores

Conceitos **source**, **sink**, **connector**, **topics** no ecossistema Kafka, integração com **MongoDB** e **CDC (Change Data Capture)**. Inclui MongoDB Sink e Source connectors (Apache Kafka) e uso de **Debezium** para CDC avançado.

---

## 1. Conceitos Fundamentais do Apache Kafka

### 1.1 Topics (Tópicos)

Um **topic** é um canal de dados nomeado no Kafka. É onde produtores publicam mensagens e consumidores leem.

- **Particionamento**: cada topic pode ser dividido em partições para paralelismo e escalabilidade.
- **Retenção**: as mensagens ficam armazenadas por um tempo (ou tamanho) configurável.
- **Ordenação**: garantida apenas dentro de uma mesma partição (por chave).
- **Replicação**: partições são replicadas entre brokers para tolerância a falhas.

Exemplo: topic `orders` para pedidos, `users.events` para eventos de usuário.

**Exemplo prático:**

| Topic | Descrição |
|-------|-----------|
| `inwave-mongodb.server2.eventspos` | Eventos de PDV (Point of Sale) publicados pelo Source a partir da coleção `eventsPOS`. |
| `inwave-mongodb.server2.eventscashexception` | Exceções de caixa publicadas a partir da coleção `eventsCashException`. |
| `inwave-mongodb.historical.server2.eventspos.202510` | Carga histórica de eventos POS para um período (ex.: out/2025). |

---

### 1.2 Source (Fonte)

**Source** é a origem dos dados que entram no ecossistema Kafka.

- **Producer**: aplicação que publica mensagens em topics.
- **Source connector**: componente que **puxa** dados de um sistema externo (banco, fila, API) e **publica** em um ou mais topics.  
  Ex.: MongoDB Source publica alterações do MongoDB em topics.

Ou seja: “source” = de onde os dados vêm antes de chegarem ao Kafka (sistema externo + producer ou connector).

---

### 1.3 Sink (Sumidouro)

**Sink** é o destino final dos dados que saem do Kafka.

- **Consumer**: aplicação que lê mensagens de topics.
- **Sink connector**: componente que **consome** de topics e **escreve** em um sistema externo (banco, data lake, API).  
  Ex.: MongoDB Sink consome de topics e grava em coleções MongoDB.

Ou seja: “sink” = para onde os dados vão depois de saírem do Kafka (sistema externo + consumer ou connector).

---

### 1.4 Connector (Conector)

**Connector** é um componente do **Kafka Connect** que automatiza a integração entre Kafka e sistemas externos, sem escrever producers/consumers manualmente.

- **Kafka Connect**: framework da Apache Kafka para conectar fontes e destinos de dados.
- **Source connector**: lê de um sistema externo → publica em topics.
- **Sink connector**: lê de topics → escreve em um sistema externo.

Características comuns:

- Configuração via JSON/REST (sem código).
- Escalabilidade (tasks, workers).
- Offset/checkpoint para retomada.
- Suporte a diferentes formatos (JSON, Avro, etc.).

---

## 2. MongoDB no Contexto de Integração

- **Documentos**: dados em BSON (JSON-like).
- **Coleções**: equivalente a “tabelas”; são o alvo típico de Sink e a origem de Source.
- **Replica set / Change streams**: permitem capturar alterações em tempo real (base para CDC com Debezium ou Source nativo).

Os conectores MongoDB para Kafka fazem a ponte entre **coleções** e **topics**.

**Exemplo (estrutura tipo InWave, mockado):** banco `server2`, coleções `eventsPOS` (eventos de PDV) e `eventsCashException` (exceções de caixa). O Source publica em topics como `inwave-mongodb.server2.eventspos` e `inwave-mongodb.server2.eventscashexception`; o Sink consome esses topics e grava em tabelas Iceberg no S3 (ver seção 8).

---

## 3. CDC (Change Data Capture)

**CDC** é a técnica de capturar apenas **mudanças** (insert, update, delete) em um repositório de dados e propagá-las para outros sistemas.

- **Vantagens**:  
  - Tempo real ou near real-time.  
  - Menor carga no sistema de origem (só mudanças).  
  - Menor volume de dados que uma cópia total.
- **Formas comuns**:  
  - Log-based: ler log de transações (oplog no MongoDB, WAL no Postgres).  
  - Trigger-based: triggers no banco.  
  - Polling: consultas periódicas por “última alteração”.

No MongoDB, **Change Streams** e o **oplog** (em replica sets) são a base para CDC log-based, usado por ferramentas como **Debezium**.

**Exemplo prático (tipo InWave):** o Source usa `startup.mode: copy_existing` para uma carga inicial e depois escuta as mudanças (Change Streams). Pipelines de filtro (ex.: `datetime >= X`, `store.idx != 0`) limitam quais documentos entram no Kafka. O Sink downstream usa o campo `operation` (U/D) para aplicar upsert ou delete nas tabelas Iceberg (ver seção 8).

---

## 4. MongoDB Source Connector

**Função**: publicar alterações das coleções MongoDB em **Kafka topics**.

- **Entrada**: coleções MongoDB (insert, update, delete).
- **Saída**: mensagens em topics Kafka (uma topic por coleção ou por banco/coleção, conforme configuração).
- **Mecanismo**:  
  - Pode usar **Change Streams** (recomendado) ou **oplog** (replica set).  
  - **Debezium MongoDB Connector** usa oplog/change streams e formata eventos em um envelope CDC padronizado (schema + payload “before”/“after”).

Formato típico de evento (ex.: Debezium):

- `before`: estado anterior do documento (update/delete).
- `after`: estado novo (insert/update).
- Metadados: operação (c, u, d), timestamp, source (db, collection), etc.

Caso de uso: replicar MongoDB → Kafka para processamento em tempo real, analytics, ou alimentar outro banco via Sink.

**Exemplo de configuração (Source tipo InWave, dados mockados):**

```json
{
  "name": "inwave-mongodb-source-eventspos",
  "config": {
    "connector.class": "com.mongodb.kafka.connect.MongoSourceConnector",
    "connection.uri": "mongodb://usuario_app:***@mongodb.example.com:27017/?authSource=admin",
    "database": "server2",
    "collection": "eventsPOS",
    "topic.prefix": "inwave-mongodb",
    "startup.mode": "copy_existing",
    "copy.existing.pipeline": "[{\"$match\":{\"datetime\":{\"$gte\":1765670400000},\"store.idx\":{\"$nin\":[0]}}}]",
    "pipeline": "[{\"$match\":{\"fullDocument.datetime\":{\"$gte\":1765670400000},\"fullDocument.store.idx\":{\"$nin\":[0]}}}]",
    "publish.full.document.only": true,
    "tasks.max": "4",
    "batch.size": "3000"
  }
}
```

- **connection.uri**: substituído por placeholder em produção; aqui mockado.
- **topic.prefix**: as mensagens vão para topics como `inwave-mongodb.server2.eventspos`.
- **pipeline** / **copy.existing.pipeline**: filtram por `datetime` e excluem `store.idx = 0` (ex.: lojas inativas).

---

## 5. MongoDB Sink Connector

**Função**: consumir mensagens de **Kafka topics** e escrever em **coleções MongoDB**.

- **Entrada**: mensagens de um ou mais topics.
- **Saída**: documentos inseridos/atualizados/removidos em coleções MongoDB.
- **Comportamento**:  
  - Mapeamento topic → coleção (por nome ou por configuração).  
  - Pode fazer insert ou upsert (ex.: por `_id` ou chave configurável).  
  - Suporte a delete quando a mensagem indicar remoção (ex.: envelope CDC com `op=d`).

Quando a origem for um Source + CDC (ex.: Debezium), o Sink aplica as operações (insert/update/delete) de forma consistente com os eventos.

Caso de uso: Kafka como hub; outros sistemas publicam em topics; MongoDB Sink consolida dados em coleções para servir aplicações ou analytics.

**Exemplo de configuração (Sink tipo InWave para Iceberg, dados mockados):**

```json
{
  "name": "inwave-iceberg-sink-historical",
  "config": {
    "connector.class": "io.tabular.iceberg.connect.IcebergSinkConnector",
    "tasks.max": 1,
    "topics.regex": "^inwave-mongodb.server2.*",
    "iceberg.tables.auto-create-enabled": true,
    "iceberg.tables.route-field": "table",
    "iceberg.tables.cdc-field": "operation",
    "iceberg.tables.default-id-columns": "_id",
    "iceberg.table.server2.eventspos.partition-by": "day(datetime)",
    "iceberg.catalog.warehouse": "s3a://123456789012-mycompany-lakehouse",
    "iceberg.catalog.catalog-impl": "org.apache.iceberg.aws.glue.GlueCatalog"
  }
}
```

- **topics.regex**: consome todos os topics que batem com `inwave-mongodb.server2.*` (ex.: eventspos, eventscashexception).
- **route-field**: usa o campo `table` da mensagem para rotear para a tabela Iceberg correta (ex.: `server2.eventspos`).
- **cdc-field**: usa o campo `operation` (U = upsert, D = delete) para aplicar CDC.
- **warehouse**: bucket S3 mockado; em produção usar o bucket real do ambiente.

---

## 6. Debezium e CDC Avançado

**Debezium** é uma plataforma de CDC open source sobre Kafka Connect.

- **Debezium MongoDB Connector**:  
  - Lê do oplog ou Change Streams.  
  - Gera eventos em formato **CDC** (schema + payload com `before`/`after`, `op`, `ts_ms`, etc.).  
  - Publica em topics Kafka (geralmente um topic por coleção ou por “logical name”).

Vantagens no contexto “MongoDB + Kafka”:

- Schema evolutivo (ex.: Apicurio Registry).
- Recuperação e replay a partir de offsets.
- Suporte a snapshot inicial (cópia completa) + streaming de mudanças.
- Formato padronizado para qualquer Sink (MongoDB ou outro) interpretar insert/update/delete.

Fluxo típico: **MongoDB (origem) → Debezium MongoDB (Source) → topics Kafka → MongoDB Sink (ou outro Sink)**.

---

## 7. Fluxo de Dados Ponta a Ponta (Resumo)

| Direção              | Componente              | Entrada           | Saída        |
|----------------------|-------------------------|-------------------|-------------|
| Sistema → Kafka      | Source connector        | MongoDB (coleções)| Kafka topics|
| Kafka → Sistema      | Sink connector          | Kafka topics      | MongoDB (coleções) |
| CDC avançado (MongoDB)| Debezium MongoDB (Source) | Change Streams/oplog | Topics com eventos CDC |

**Exemplo de pipeline CDC:**

1. Aplicação escreve em MongoDB.
2. Debezium (MongoDB Source) captura as mudanças e publica em topics (ex.: `db.inventory.customers`).
3. MongoDB Sink (ou outro Sink) consome esses topics e atualiza outro MongoDB (ou outro destino).

**Exemplo com estrutura tipo InWave:** MongoDB (`server2.eventsPOS` / `server2.eventsCashException`) → Source Connector → topics `inwave-mongodb.server2.*` → Iceberg Sink → S3 + Glue. Detalhes e dados mockados na **seção 8**.

---

## 8. Exemplos Práticos – Pipeline tipo InWave (dados mockados)

Esta seção usa uma arquitetura inspirada em **MongoDB → Kafka Connect → Topics → Iceberg (S3/Glue)**, com **dados e identificadores sensíveis mockados**.

### 8.1 Visão do pipeline

```
[MongoDB]  server2.eventsPOS, server2.eventsCashException
     │
     ▼  MongoDB Source Connectors (CDC / copy_existing)
[Kafka]   inwave-mongodb.server2.eventspos
          inwave-mongodb.server2.eventscashexception
     │
     ▼  Iceberg Sink Connector (topics.regex)
[AWS]     S3 (lakehouse) + Glue Catalog → tabelas Iceberg
```

- **Source**: dois conectores (eventspos e eventscashexception) leem do mesmo cluster MongoDB, bancos/coleções diferentes.
- **Topics**: um topic por origem (ex.: `inwave-mongodb.server2.eventspos`).
- **Sink**: um conector consome todos os topics que batem com `inwave-mongodb.server2.*` e grava em tabelas Iceberg particionadas por dia.

### 8.2 Documento mockado no MongoDB (eventsPOS)

Exemplo de documento que poderia existir na coleção `server2.eventsPOS` (valores fictícios):

```json
{
  "_id": "507f1f77bcf86cd799439011",
  "datetime": 1738656000000,
  "store": { "idx": 100 },
  "pos": { "code": "POS-01", "idx": 1 },
  "cash_box_idx": 1,
  "products": [
    { "code": "PROD-001", "description": "Produto A", "quantity": 2.0, "total_value": 19.98 }
  ],
  "time zone": "America/Sao_Paulo",
  "store status": "open"
}
```

O Source pode aplicar **transforms** (renomear `POS` → `pos`, `time zone` → `time_zone`, flatten, etc.) e adicionar campos como `operation: "U"` e `table: "server2.eventspos"` antes de publicar no Kafka.

### 8.3 Mensagem mockada no topic (após transforms)

Exemplo do valor que pode chegar no topic `inwave-mongodb.server2.eventspos` (Avro/JSON, dados mockados):

```json
{
  "operation": "U",
  "table": "server2.eventspos",
  "_id": "507f1f77bcf86cd799439011",
  "datetime": 1738656000000,
  "store_idx": 100,
  "pos_code": "POS-01",
  "pos_idx": 1,
  "cash_box_idx": 1,
  "products": [
    { "code": "PROD-001", "description": "Produto A", "quantity": 2.0, "total_value": 19.98 }
  ],
  "time_zone": "America/Sao_Paulo",
  "store_status": "open"
}
```

O Sink usa `table` para rotear e `operation` para CDC (upsert/delete); `_id` é usado como coluna de identidade nas tabelas Iceberg.

### 8.4 Evento CDC mockado (formato Debezium-like)

Se fosse usado Debezium em vez do MongoDB Kafka Source nativo, um evento de **update** poderia ter esta forma (dados mockados):

```json
{
  "before": {
    "_id": "507f1f77bcf86cd799439011",
    "datetime": 1738656000000,
    "store": { "idx": 100 },
    "products": []
  },
  "after": {
    "_id": "507f1f77bcf86cd799439011",
    "datetime": 1738656000000,
    "store": { "idx": 100 },
    "products": [
      { "code": "PROD-001", "description": "Produto A", "quantity": 2.0, "total_value": 19.98 }
    ]
  },
  "source": {
    "version": "2.4.0",
    "connector": "mongodb",
    "name": "inwave-mongodb",
    "db": "server2",
    "collection": "eventsPOS"
  },
  "op": "u",
  "ts_ms": 1738656123456
}
```

- `op`: `c` (create), `u` (update), `d` (delete).
- `before` / `after`: estado anterior e novo do documento.
- **Nota**: URIs, hosts, versões e IDs acima são exemplos; em produção usar valores reais e proteger credenciais.

### 8.5 Dados sensíveis – o que mockar em documentação

Em exemplos e templates, substituir sempre:

| Dado real (não documentar) | Exemplo mockado |
|----------------------------|-----------------|
| Connection string MongoDB com usuário/senha | `mongodb://usuario_app:***@mongodb.example.com:27017` |
| Bucket S3 da conta | `123456789012-mycompany-lakehouse` |
| IDs de conta AWS | `123456789012` |
| Hosts e IPs internos | `mongodb.example.com`, `kafka.example.com` |
| Schema Registry URL interno | `http://localhost:8081` ou `http://schema-registry.example.com:8081` |

Manter em repositórios apenas arquivos `.dist` (templates) e ignorar os `.json` com valores reais (ex.: em `.gitignore`: `connectors_inwave/*.json`).

---

## 9. Glossário Rápido

| Termo        | Significado |
|-------------|-------------|
| **Topic**   | Canal de mensagens no Kafka (nomeado e particionado). |
| **Source**  | Origem dos dados (sistema externo + producer/Source connector). |
| **Sink**    | Destino dos dados (consumer/Sink connector + sistema externo). |
| **Connector** | Componente Kafka Connect que integra Kafka a um sistema (Source ou Sink). |
| **CDC**     | Captura e propagação apenas de mudanças (insert/update/delete). |
| **MongoDB Source** | Conector que publica alterações de coleções MongoDB em topics. |
| **MongoDB Sink**   | Conector que grava mensagens de topics em coleções MongoDB. |
| **Debezium**      | Plataforma CDC sobre Kafka Connect; para MongoDB usa oplog/Change Streams. |
