# Amazon CloudWatch e AWS CloudTrail

# 🌩️ Amazon CloudWatch

O **Amazon CloudWatch** é um serviço da AWS usado para **monitoramento**, **observabilidade** e **alertas**.  
Ele coleta métricas, logs e eventos de praticamente qualquer serviço AWS — além de aplicações próprias.

O CloudWatch não altera nada na sua infraestrutura; ele apenas **observa, registra e alerta**.

---

### 1. **Métricas (Metrics)**

São valores numéricos coletados ao longo do tempo.  
Exemplos:

- uso de CPU de uma EC2
- quantidade de erros 5xx em uma API
- duração de um job Glue
- quantidade de requisições S3

Essas métricas podem ser exibidas em **dashboards**.

---

### 2. **Logs (CloudWatch Logs)**

É onde ficam os logs de:

- Jobs do AWS Glue
- Lambda
- VPC Flow Logs
- Aplicações customizadas
- S3 Access Logs (se habilitado)
- ECS / EKS

Você pode visualizar logs, filtrar, fazer buscas e criar alarmes baseados em padrões.

---

### 3. **Alarmes (CloudWatch Alarms)**

Permitem reagir a uma métrica que atingiu um limite.

Exemplos:

- CPU > 80% por 5 min → envia alerta pro SNS
- Glue Job falhou → notificação
- Latência da API muito alta → Slack

Alarmes **não tomam decisões de infraestrutura** (como autoscaling), mas podem **disparar** serviços que tomam.

---

### 4. **Events / EventBridge**

CloudWatch Events (hoje integrado ao EventBridge) permite **reagir a eventos em tempo real**.

Exemplo:

- Quando um Glue Job terminar → executar outra Lambda
- Quando um arquivo entrar no S3 → disparar workflow

Isso gera automações orientadas a eventos.

---

## Como o CloudWatch Funciona (Arquitetura Lógica)

Ele trabalha em **três camadas principais**:

1. **Coleta** → logs e métricas chegam de serviços AWS ou apps.
2. **Armazenamento** → métricas ficam em time-series DB interno; logs ficam no CloudWatch Logs.
3. **Ação** → dashboards, alarmes, triggers, análises.

O CloudWatch é como um **painel de controle operacional**.

---

# 🕵️‍♂️ AWS CloudTrail

O **AWS CloudTrail** registra **eventos de API** na sua conta AWS.  
Enquanto o CloudWatch observa a operação, **o CloudTrail observa quem fez o quê**, quando e de onde.

---

## Para Que Serve

- Auditoria
- Segurança
- Governança
- Rastreabilidade
- Investigações

Se algo aconteceu na sua conta. Se alguém criou um bucket, deletou uma role, executou um Glue Job, o CloudTrail sabe.

---

## Como Ele Funciona (Metadados)

O CloudTrail trabalha com três conceitos:

### 1. **Event Logs**

Cada ação gera um evento JSON contendo:

- Quem fez (IAM User / Role / Serviço)
- Quando fez (timestamp)
- De onde veio (IP, região)
- Qual API foi chamada
- Qual recurso foi modificado
- Resultado da chamada

Exemplo: `StartJobRun` no Glue, `PutObject` no S3, `CreateTable` no Athena, etc.

---

### 2. **Trails**

Um **Trail** define para onde enviar esses eventos:

- S3 (mais comum)
- CloudWatch Logs
- EventBridge

Também define **quais tipos de eventos registrar**:

- Management events (IAM, S3, Glue, etc.)
- Data events (acesso detalhado ao S3, Lambda invoke)
- Insights events (anomalias detectadas automaticamente)

---

### 3. **Insights**

O CloudTrail pode detectar:

- aumento anormal de `Delete`
- volume anormal de `StartJobRun`
- mudanças incomuns em políticas IAM

Funciona como **comportamento anômalo**.

---

# 🔥 Como CloudWatch e CloudTrail se Complementam

A forma mais simples de entender:

- **CloudTrail diz _o que aconteceu_ e _quem fez_.**
- **CloudWatch diz _como o sistema está_ e _o que está dando errado_.**

Exemplo:

- CloudTrail mostra:  
    “Usuário X chamou UpdateTable no Glue Catalog às 15:38”.
- CloudWatch mostra:  
    “O job do Glue começou a falhar após essa mudança”.

Ou seja:

**CloudTrail = Auditoria**  
**CloudWatch = Monitoramento**

