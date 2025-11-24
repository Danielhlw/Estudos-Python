
#TODO
- Como funciona, o que é, como habilitar...
# Desabilitar a regra do EventBridge
aws events disable-rule --name nucleo-sharepoint-ingestion-schedule

# Verificar status
aws events describe-rule --name nucleo-sharepoint-ingestion-schedule