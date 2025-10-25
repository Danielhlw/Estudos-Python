import json

texto = '{"nome": "Daniel", "idade": 22}'
dados = json.loads(texto)  
# passa de string para dict
print(dados["nome"])

texto_json = json.dumps(dados, indent=4)
# passa de dict para string json 
print(texto_json)
