import requests
import json
response_API = requests.get('https://www.tbca.net.br/base-dados/busca_componente.php') //Conectando-se API
#print(response_API.status_code)
data = response_API.text //Extraindo dados da API
parse_json = json.loads(data) // Analisando os dados extraídos(convertê-los e decodificá-los) 
active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active'] // extrair e imprimir os dados usando os valores-chave do objeto JSON
print("Active cases in South Andaman:", active_case)


import requests
import json
response_API = requests.get('https://www.tbca.net.br/base-dados/busca_componente.php')
#print(response_API.status_code)
data = response_API.text
parse_json = json.loads(data)
info = parse_json['description']
print("Info about API:\n", info)
key = parse_json['parameters']['key']['description']
print("\nDescription about the key:\n",key)

//Fetch Grupo Alimentar;
//Fetch Tipo do Alimento;
//Fetch Composição do ALimento;
