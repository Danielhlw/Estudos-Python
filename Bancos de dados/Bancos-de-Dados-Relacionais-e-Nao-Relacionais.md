# Bancos de Dados: Relacionais e Não Relacionais

## Índice

1. [Bancos de Dados Relacionais](#1-bancos-de-dados-relacionais)
2. [Bancos de Dados Não Relacionais (NoSQL)](#2-bancos-de-dados-não-relacionais-nosql)
3. [Resumo Comparativo](#3-resumo-comparativo)

---

## 1. Bancos de Dados Relacionais

Bancos de dados **relacionais** armazenam dados em **tabelas** com **linhas** (registros) e **colunas** (atributos). O relacionamento entre tabelas é feito por **chaves** (primária e estrangeira), e as consultas seguem a linguagem **SQL** (Structured Query Language).

### Características principais

- **Esquema fixo**: estrutura das tabelas definida com antecedência
- **ACID**: Atomicidade, Consistência, Isolamento e Durabilidade
- **Integridade referencial**: garantia de consistência entre tabelas relacionadas
- **SQL**: linguagem padrão para consultas e manipulação

### Categorias de bancos relacionais

Os bancos relacionais podem ser classificados pela forma de implantação e operação:

| Categoria | Descrição | Exemplos |
|-----------|-----------|----------|
| **Tradicional (on-premise)** | Instalados e gerenciados na própria infraestrutura (servidor local ou datacenter). Controle total sobre hardware e configuração. | PostgreSQL, MySQL, Oracle Database, SQL Server (instalação local) |
| **Na nuvem (cloud)** | Oferecidos como serviço por provedores; a infraestrutura é gerenciada por eles. Escalabilidade, backup e alta disponibilidade costumam ser simplificados. | Amazon RDS, Azure SQL Database, Google Cloud SQL, Oracle Cloud Autonomous Database |
| **Embutido (embedded)** | Rodam dentro da aplicação, sem servidor separado. Arquivo único ou biblioteca; ideais para apps desktop, mobile ou protótipos. | SQLite, H2, DuckDB |
| **Gerenciado (managed)** | Serviço em que o provedor cuida de atualizações, patches e, em muitos casos, backups. Pode ser na nuvem ou em ambientes híbridos. | RDS, Azure SQL, Cloud SQL (também se encaixam em “na nuvem”) |

- **Tradicional**: melhor quando há requisitos rígidos de compliance, dados sensíveis que não podem sair do datacenter ou necessidade de controle total.
- **Na nuvem**: ideal para escalar rápido, reduzir custo de operação e aproveitar backups e réplicas gerenciadas.
- **Embutido**: útil em aplicações que não precisam de servidor dedicado (apps locais, testes, IoT).

### Exemplo: SQLite (relacional embutido)

O **SQLite** é um banco relacional **embutido**, leve e que não precisa de servidor. Muito usado em aplicações desktop, mobile e protótipos.

**Exemplo em Python:**

```python
import sqlite3

# Conectar ao banco (cria o arquivo se não existir)
conn = sqlite3.connect('exemplo_relacional.db')
cursor = conn.cursor()

# Criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        valor REAL,
        data TEXT,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
''')

# Inserir dados
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", ("Maria Silva", "maria@email.com"))
cursor.execute("INSERT INTO pedidos (cliente_id, valor, data) VALUES (1, 150.00, '2025-02-26')")

# Consulta com JOIN (relacionamento entre tabelas)
cursor.execute('''
    SELECT c.nome, p.valor, p.data
    FROM clientes c
    JOIN pedidos p ON c.id = p.cliente_id
''')
for linha in cursor.fetchall():
    print(linha)

conn.commit()
conn.close()
```

**Saída esperada:** `('Maria Silva', 150.0, '2025-02-26')`

---

## 2. Bancos de Dados Não Relacionais (NoSQL)

"NoSQL" significa "Not Only SQL". Esses bancos não usam obrigatoriamente tabelas e SQL; os dados podem ser armazenados em formatos como documentos, chave-valor, grafos ou colunas, dependendo do tipo.

### 2.1 Banco de documentos (Document Store)

Armazenam dados em **documentos** (geralmente JSON/BSON). Cada documento pode ter estrutura diferente. Ideais para dados semi-estruturados e hierárquicos.

**Exemplo: MongoDB (documentos)**

```python
# Instale: pip install pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['exemplo_nosql']
colecao = db['usuarios']

# Inserir um documento (estrutura flexível)
colecao.insert_one({
    "nome": "João Santos",
    "email": "joao@email.com",
    "idade": 28,
    "endereco": {
        "cidade": "São Paulo",
        "uf": "SP"
    },
    "tags": ["python", "dev"]
})

# Buscar documentos
for doc in colecao.find({"endereco.cidade": "São Paulo"}):
    print(doc)
```

---

### 2.2 Banco chave-valor (Key-Value)

Armazenam dados como pares **chave → valor**. Muito rápidos para leitura/escrita e cache. Não há esquema; o valor pode ser string, número ou objeto serializado.

**Exemplo: Redis (chave-valor)**

```python
# Instale: pip install redis
import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Guardar e recuperar valores
r.set("usuario:1001:nome", "Ana Costa")
r.set("usuario:1001:ultimo_acesso", "2025-02-26 10:00:00")

nome = r.get("usuario:1001:nome")
print(nome)  # Ana Costa

# Exemplo com hash (múltiplos campos de um mesmo "objeto")
r.hset("produto:501", mapping={"nome": "Notebook", "preco": "3500", "estoque": "10"})
produto = r.hgetall("produto:501")
print(produto)  # {'nome': 'Notebook', 'preco': '3500', 'estoque': '10'}
```

---

### 2.3 Banco de colunas (Column Family / Wide Column)

Organizam dados por **famílias de colunas**, otimizados para consultas em grandes volumes e análise. Cada linha pode ter um conjunto diferente de colunas.

**Exemplo: Apache Cassandra (colunas)**

```python
# Instale: pip install cassandra-driver
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

# Criar keyspace e tabela
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS exemplo
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
""")
session.set_keyspace('exemplo')

session.execute("""
    CREATE TABLE IF NOT EXISTS sensores (
        sensor_id UUID PRIMARY KEY,
        tipo TEXT,
        valor DECIMAL,
        timestamp TIMESTAMP
    )
""")

# Inserir e consultar
from cassandra.util import uuid_from_time
import datetime

session.execute(
    "INSERT INTO sensores (sensor_id, tipo, valor, timestamp) VALUES (%s, %s, %s, %s)",
    (uuid_from_time(datetime.datetime.now()), "temperatura", 23.5, datetime.datetime.now())
)

rows = session.execute("SELECT * FROM sensores")
for row in rows:
    print(row)
```

---

### 2.4 Banco de grafos (Graph)

Armazenam **nós** (entidades) e **arestas** (relacionamentos). Ideais para redes sociais, recomendação e tudo que depende de relações complexas entre entidades.

**Exemplo: Neo4j (grafos)**

```python
# Instale: pip install neo4j
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "senha"))

def criar_pessoa_e_amizade(tx, nome1, nome2):
    tx.run(
        "CREATE (a:Pessoa {nome: $nome1})-[:AMIGO_DE]->(b:Pessoa {nome: $nome2})",
        nome1=nome1, nome2=nome2
    )

def buscar_amigos(tx, nome):
    result = tx.run(
        "MATCH (p:Pessoa {nome: $nome})-[:AMIGO_DE]-(amigo) RETURN amigo.nome AS nome",
        nome=nome
    )
    return [record["nome"] for record in result]

with driver.session() as session:
    session.execute_write(criar_pessoa_e_amizade, "Carlos", "Beatriz")
    amigos = session.execute_read(buscar_amigos, "Carlos")
    print("Amigos de Carlos:", amigos)

driver.close()
```

**Saída esperada:** `Amigos de Carlos: ['Beatriz']`

---

## 3. Resumo Comparativo

| Tipo              | Modelo        | Exemplo   | Melhor para                          |
|-------------------|---------------|-----------|--------------------------------------|
| Relacional        | Tabelas + SQL | SQLite    | Dados estruturados, integridade, relatórios |
| Documentos        | JSON/BSON     | MongoDB   | Conteúdo flexível, catálogos, perfis |
| Chave-valor       | Key → Value   | Redis     | Cache, sessões, filas                |
| Colunas           | Famílias      | Cassandra | Escala horizontal, séries temporais  |
| Grafos            | Nós + arestas | Neo4j     | Redes, recomendações, caminhos       |

---

## Quando usar cada um?

- **Relacional (ex.: SQLite, PostgreSQL, MySQL)**  
  Quando você precisa de transações confiáveis, relatórios complexos e dados bem definidos (ex.: ERP, sistemas financeiros).

- **Documentos (ex.: MongoDB)**  
  Quando o formato dos dados varia ou é hierárquico (ex.: formulários dinâmicos, conteúdo de blog, perfis de usuário).

- **Chave-valor (ex.: Redis)**  
  Quando a prioridade é velocidade e simplicidade (ex.: cache, sessão, filas simples).

- **Colunas (ex.: Cassandra)**  
  Quando há muito volume de dados e necessidade de escalar horizontalmente (ex.: logs, métricas, IoT).

- **Grafos (ex.: Neo4j)**  
  Quando o foco são relacionamentos e caminhos entre entidades (ex.: redes sociais, detecção de fraude, recomendação).

---

*Documento criado para fins de estudo. Para usar MongoDB, Redis, Cassandra ou Neo4j, é necessário ter o servidor correspondente instalado e em execução.*
