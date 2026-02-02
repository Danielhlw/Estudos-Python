# Tutorial: AWS Athena + S3 para Iniciantes em Engenharia de Dados

## Visão Geral do Fluxo

Este tutorial ensina como criar um pipeline básico de dados na AWS:
1. **S3**: Armazenar arquivos de dados (ex: CSV, JSON)
2. **Glue Crawler**: "Farejar" os dados e descobrir sua estrutura
3. **Glue Data Catalog**: Criar metadados (schema) das tabelas
4. **Athena**: Consultar os dados usando SQL

**Conceito Importante**: O Athena não armazena os dados reais. Ele é um serviço de consulta que lê os dados diretamente do S3 usando os metadados criados pelo Glue Catalog. É como ter um "banco de dados virtual" que aponta para arquivos no S3.

---

## Passo 1: Criar um Bucket no S3

O S3 (Simple Storage Service) é o serviço de armazenamento de objetos da AWS. Um **bucket** é como uma "pasta" na nuvem onde você armazena seus arquivos.

### Como criar:

1. Acesse o [console do S3](https://us-east-2.console.aws.amazon.com/s3/bucket/create?region=us-east-2)
2. Clique em "Create bucket"
3. Configure:
   - **Região**: Escolha uma região (ex: us-east-2)
   - **Nome do bucket**: Deve ser único globalmente (ex: `meu-bucket-dados-2024`)
4. Deixe as outras configurações no padrão e clique em "Create bucket"

---

## Passo 2: Fazer Upload de Arquivos para o Bucket

Agora vamos adicionar dados ao bucket. Para este tutorial, use um arquivo CSV como exemplo.

### Como fazer upload:

1. Entre no bucket que você acabou de criar
2. Clique em "Upload"
3. Arraste o arquivo CSV ou clique em "Add files" para selecionar
4. Clique em "Upload" para finalizar

**Dica**: Organize seus arquivos em pastas dentro do bucket (ex: `dados/2024/janeiro/vendas.csv`) para facilitar a organização.

---

## Passo 3: Configurar o Athena (Primeira Vez)

O Athena é um serviço de consulta interativa que permite usar SQL padrão para analisar dados diretamente no S3.

### Configuração inicial:

1. Acesse o [console do Athena](https://us-east-2.console.aws.amazon.com/athena/home?region=us-east-2#/landing-page)
2. Na primeira vez, você precisará configurar um local para salvar os resultados das consultas:
   - Clique em "Edit settings"
   - Navegue até o S3 e escolha um bucket (pode ser o mesmo que você criou ou criar um novo para resultados)
   - Salve as configurações

**Por que isso é necessário?**: O Athena precisa de um local no S3 para salvar os resultados das suas consultas SQL.

---

## Passo 4: Usar o Glue Crawler para Descobrir a Estrutura dos Dados

O **AWS Glue Crawler** é uma ferramenta que "fareja" seus arquivos no S3 e descobre automaticamente:
- A estrutura dos dados (colunas, tipos de dados)
- O formato dos arquivos (CSV, JSON, Parquet, etc.)
- Cria metadados no **Glue Data Catalog**

O Data Catalog funciona como um "catálogo" de metadados - ele não armazena os dados, apenas informações sobre onde estão e como estão organizados.

### Como criar e configurar o Crawler:

1. No console da AWS, procure por "Glue" e acesse o serviço
2. No menu lateral, clique em "Crawlers"
3. Clique em "Create crawler"

#### 4.1. Nome do Crawler
- Dê um nome descritivo (ex: `crawler-vendas-csv`)

#### 4.2. Data Source (Fonte de Dados)
- Clique em "Add a data source"
- Selecione "S3" como tipo
- Configure o caminho do bucket:
  - Se seus arquivos estão na raiz: `s3://nome-do-seu-bucket/`
  - Se estão em uma pasta: `s3://nome-do-seu-bucket/pasta/`
- Avance para a próxima etapa

#### 4.3. IAM Role (Permissões)
- O Crawler precisa de permissões para acessar o S3 e criar tabelas no Glue Catalog
- Crie uma nova IAM Role ou selecione uma existente
- Se criar nova, use o prefixo sugerido (ex: `AWSGlueServiceRole-`)

#### 4.4. Output (Saída - Database)
- O Crawler precisa saber onde criar a tabela com os metadados
- Selecione um banco de dados existente ou crie um novo
- **O que é um Database no Glue?**: É uma coleção de tabelas (metadados). Pense como um "esquema" em um banco de dados tradicional
- Exemplo de nome: `meu_database_dados`

#### 4.5. Revisar e Criar
- Revise todas as configurações
- Clique em "Create crawler"
- Após criar, selecione o crawler e clique em "Run crawler"

**O que acontece agora?**
- O Crawler vai analisar seus arquivos no S3
- Ele vai inferir o schema (estrutura) dos dados
- Criará uma tabela no Glue Data Catalog com os metadados
- Essa tabela conterá informações como: nomes das colunas, tipos de dados, localização dos arquivos no S3

---

## Passo 5: Consultar os Dados no Athena

Agora que o Crawler criou os metadados no Data Catalog, você pode consultar os dados usando SQL no Athena!

### Como fazer uma consulta:

1. Volte para o [console do Athena](https://us-east-2.console.aws.amazon.com/athena/home?region=us-east-2#/landing-page)
2. No painel lateral esquerdo, você verá:
   - **Databases**: Selecione o database que você criou
   - **Tables**: Você verá a tabela criada pelo Crawler
3. Clique na tabela para ver sua estrutura (colunas e tipos)
4. No editor de consultas, escreva uma query SQL:

```sql
-- Exemplo: Ver todas as linhas
SELECT * FROM "meu_database_dados"."nome_da_tabela" LIMIT 10;

-- Exemplo: Contar registros
SELECT COUNT(*) FROM "meu_database_dados"."nome_da_tabela";

-- Exemplo: Filtrar dados
SELECT coluna1, coluna2 
FROM "meu_database_dados"."nome_da_tabela" 
WHERE coluna1 > 100;
```

5. Clique em "Run" para executar a consulta

**Lembre-se**: 
- Os dados continuam no S3
- O Athena apenas lê os dados usando os metadados do Glue Catalog
- Os resultados da consulta são salvos no bucket configurado no Passo 3

---

## Diagrama da Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                    ARQUIVOS DE DADOS                            │
│              (CSV, JSON, Parquet, etc.)                         │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ Upload
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                         S3 BUCKET                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  s3://meu-bucket-dados/                                   │  │
│  │    ├── vendas.csv                                         │  │
│  │    ├── clientes.json                                      │  │
│  │    └── produtos/                                          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                    (Armazenamento de Dados Brutos)              │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ Crawler analisa
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                    GLUE CRAWLER                                 │
│  • Lê os arquivos no S3                                         │
│  • Infere schema (colunas, tipos)                               │
│  • Detecta formato dos dados                                    │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ Cria metadados
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  GLUE DATA CATALOG                               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Database: meu_database_dados                             │  │
│  │    └── Table: vendas                                      │  │
│  │         ├── Colunas: id, data, valor, cliente            │  │
│  │         ├── Tipos: int, date, decimal, string            │  │
│  │         └── Localização: s3://bucket/vendas.csv           │  │
│  └──────────────────────────────────────────────────────────┘  │
│              (Catálogo de Metadados - Não armazena dados)       │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ Consulta usando metadados
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                        ATHENA                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  SELECT * FROM vendas WHERE valor > 1000;                │  │
│  └──────────────────────────────────────────────────────────┘  │
│  • Executa SQL padrão                                           │
│  • Lê dados diretamente do S3                                   │
│  • Usa metadados do Glue Catalog                                │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           │ Salva resultados
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              S3 BUCKET (Resultados)                              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  s3://bucket-resultados/athena-results/                   │  │
│  │    └── query-results-2024-01-15.csv                       │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘

LEGENDA:
  →  Fluxo de dados
  ↓  Processamento/Ação
  ┌─┐ Componentes do sistema
```

## Resumo do Fluxo Completo

1. **Armazenamento**: Arquivos são enviados para o S3 (data lake)
2. **Descoberta**: Glue Crawler analisa os arquivos e descobre sua estrutura
3. **Catalogação**: Metadados são criados no Glue Data Catalog
4. **Consulta**: Athena usa os metadados para consultar os dados com SQL
5. **Resultados**: Os resultados das consultas são salvos de volta no S3

---

## Conceitos Importantes para Engenharia de Dados

- **Data Lake**: O S3 funciona como um data lake - armazena dados brutos em qualquer formato
- **Schema-on-Read**: O Athena usa "schema on read" - a estrutura é definida na hora da leitura, não na escrita
- **Metadados**: Informações sobre os dados (estrutura, localização) sem armazenar os dados em si
- **Separação de Armazenamento e Computação**: Dados no S3, processamento no Athena (arquitetura moderna de dados)

---

## Próximos Passos

- Aprender sobre particionamento de dados no S3
- Otimizar consultas usando formatos como Parquet
- Configurar crawlers para múltiplos arquivos/pastas
- Integrar com outros serviços AWS (Lambda, EMR, etc.)
