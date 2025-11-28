# 📊 Amazon QuickSight

O **Amazon QuickSight** é o serviço de BI (Business Intelligence) da AWS.  
Ele permite criar:

- Dashboards
- Visualizações
- KPIs
- Análises com IA
- Exploração de dados via linguagem natural (Q)
- Painéis compartilháveis e sem servidor

O grande diferencial do QuickSight é ser **serverless**, elástico e muito mais barato que soluções tradicionais.

---

## 🔍 Componentes Principais

### 1. **Datasets**

São as fontes de dados utilizadas no dashboard.  
Você pode conectar:

- S3 (Parquet, CSV, JSON)
- Athena
- RDS / Redshift
- APIs / Glue
- Arquivos estáticos

No seu projeto, o dataset principal vem do **Athena lendo S3 Bronze/Silver**.

---

### 2. **SPICE**

É um **banco de dados in-memory** (colunar) extremamente rápido.  
Funciona assim:

- Você importa os dados para o SPICE
- O QuickSight deixa tudo otimizado em RAM
- As consultas ficam **muito mais rápidas e baratas**

Ideal para:

- Dashboards com muitos acessos
- Reduzir custo do Athena
- Dimensões e fatos prontos (Silver)

---

### 3. **Análises (Analysis)**

É onde você constrói:

- Gráficos
- Tabelas
- KPIs
- Filtros
- Controles de data

Depois, transforma isso em Dashboard.

---

### 4. **Dashboards**

A versão final que você entrega ao cliente.

- Interativo
- Filtros
- Drill-down
- Compartilhamento
- Automação via email

---

# 🧠 Amazon Q (Dentro do QuickSight)

O **Amazon Q** dentro do QuickSight é uma camada de IA que permite ao usuário **perguntar** coisas como:

> “Quais foram as vendas da loja X nos últimos 3 meses?”

e ele **gera automaticamente gráficos, tabelas e insights**.

O Q usa:

- Modelo de linguagem especializado da AWS
- Seu **dicionário de negócios** (explicações das métricas)
- Dataset SPICE preparado

---

# 🏢 Amazon Q Business

Diferente do Q do QuickSight, o **Amazon Q Business** é uma **plataforma completa de IA corporativa**.

Ele conecta com várias fontes, por exemplo:

- Documentos internos
- SharePoint
- Confluence
- Gmail
- OneDrive
- Excel
- PDFs e tabelas
- Base de conhecimento
- Dados estruturados e não estruturados

E permite que o usuário **converse com os dados da empresa inteira**, não só BI.

---

# 🔎 Diferença Rápida: Q do QuickSight vs Q Business

|Recurso|Q no QuickSight|Q Business|
|---|---|---|
|Foco|Dados analíticos (BI)|Dados da empresa como um todo|
|Dados|SPICE / Athena|SharePoint, documentos, bases internas|
|Função|Cria gráficos, KPIs e análises|Assistente corporativo completo|
|Interface|Dentro do QuickSight|Chat corporativo próprio|
|Governança|Data governance|Knowledge governance|

## 🔗 Integração: Amazon QuickSight + Amazon Q Business

O **Amazon Q Business** pode se conectar ao **Amazon QuickSight** e utilizar seus dashboards como fonte de conhecimento.  
Essa integração permite que o Q Business:

1. **Leia e indexe**:
    
    - dashboards
    - análises
    - títulos e descrições
    - campos calculados
    - dimensões e métricas
    - dicionários de negócios
    - metadados dos datasets SPICE
    
2. **Compreenda a estrutura dos dados**:
    
    - hierarquias
    - chaves
    - modelos de dados
    - métricas de negócios
    
3. **Gere respostas inteligentes**, como:
    
    - resumos automáticos do painel
    - explicação de KPIs
    - insights de crescimento
    - identificação de outliers
    - comparações históricas (com base no que o painel mostra)
    - recomendações ou alertas
      
4. **Cruze informações**:
    - dados estruturados do QuickSight
    - documentos internos (SharePoint, PDFs, Word, políticas)
    - regras de negócio

### Em uma frase:

> **Q no QuickSight = BI conversacional.  
> Q Business = Assistente corporativo inteligente.**
