## O que são S3 Tables?

Simplificando, um S3 Table é um armazenamento S3 otimizado e gerenciado para dados tabulares, com **suporte nativo ao Apache Iceberg**.

- **Apache Iceberg:** É um formato de tabela de código aberto, projetado para data lakes, que resolve muitos desafios de escalabilidade, desempenho e confiabilidade encontrados ao trabalhar com grandes volumes de dados no S3.
    
- **Armazenamento Otimizado:** O AWS criou um novo tipo de _bucket_ S3, chamado **Table Bucket**, que é especificamente otimizado para armazenar os dados e metadados de uma tabela Iceberg. Os dados subjacentes podem ser armazenados nos formatos **Apache Parquet**, Avro ou ORC.
    

---

## Principais Vantagens

A principal motivação para usar S3 Tables é a melhoria significativa no **desempenho** e a **simplificação operacional**:

- **Desempenho Otimizado:** As S3 Tables oferecem até **3x mais velocidade de consulta** e até **10x mais transações por segundo** em comparação com tabelas Iceberg que você gerencia por conta própria no S3.
    
- **Manutenção Automática:** Um dos maiores benefícios é que o AWS gerencia automaticamente as operações de manutenção das tabelas Iceberg, incluindo:
    
    - **Compactação (Compaction):** Reescreve automaticamente muitos arquivos pequenos em arquivos maiores, melhorando o desempenho da leitura.
        
    - **Gerenciamento de Snapshots:** Exclui _snapshots_ expirados.
        
    - **Remoção de Arquivos Não Referenciados:** Exclui objetos que não são mais necessários. Isso alivia os engenheiros de dados da necessidade de executar esses trabalhos de manutenção periodicamente.
        
- **Integração com AWS Analytics:** Têm integração facilitada com serviços de análise populares da AWS, como **Amazon Athena**, **Amazon Redshift**, **Amazon EMR** e **Apache Spark**.
    

---

## ⚙️ Como Funciona a Estrutura

Ao usar S3 Tables, você trabalha com três conceitos principais:

1. **Table Bucket:** É o novo tipo de _bucket_ S3, servindo como um "data warehouse" analítico que armazena várias tabelas Iceberg.
    
2. **Namespace:** Similar a um banco de dados (database), organiza as tabelas dentro do Table Bucket.
    
3. **Table:** A tabela Iceberg propriamente dita, onde os dados tabulares (transações diárias, dados de sensores, etc.) são armazenados.
    

Em essência, as S3 Tables transformam a experiência de gerenciar data lakes no S3, tornando o armazenamento de dados estruturados mais parecido com a experiência de usar um _data warehouse_ tradicional, mas mantendo a escalabilidade e o baixo custo do S3.