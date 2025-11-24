O **Apache Iceberg** é um **formato de tabela** de código aberto projetado para gerenciar coleções massivas de arquivos de dados em um _data lake_, permitindo que você os use como se fossem tabelas em um banco de dados relacional.

Ele não armazena os dados em si (que continuam sendo arquivos Parquet, Avro, etc., no S3), mas sim os **metadados** que descrevem onde esses dados estão e como eles estão estruturados.

## Como Ele Funciona (Metadados)

O Iceberg usa uma estrutura de metadados de **três níveis** para rastrear os arquivos de dados:

1. **Metadata File (Arquivo de Metadados):** Este é o **estado atual da tabela**. Ele aponta para o _snapshot_ ativo.
    
2. **Snapshot:** Um _snapshot_ representa o **estado da tabela em um ponto no tempo**. Cada _snapshot_ aponta para uma lista de **Manifest Lists**.
    
3. **Manifest List:** Uma lista que aponta para um ou mais **Manifest Files**.
    
4. **Manifest File:** Um arquivo que lista todos os **Data Files** (arquivos Parquet, ORC) que compõem a tabela naquele _snapshot_. Este arquivo também armazena estatísticas (como limites superior e inferior de colunas) sobre os dados, o que acelera o **predicate pushdown** (filtragem de dados).
    

Essa separação de dados e metadados, gerenciada de forma centralizada pelo Iceberg, é o que garante o desempenho e a confiabilidade.

O Iceberg se tornou o padrão para a construção de **Data Lakehouses**, que combinam os benefícios de um _data lake_ (escalabilidade e baixo custo) com a funcionalidade de um _data warehouse_ (confiabilidade e bom desempenho de consultas).