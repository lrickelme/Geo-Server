import requests

URL = "http://localhost:8080/geoserver/Lucas_Rickelme/wms?service=WMS&request=GetCapabilities"

response = requests.get(URL)

if response.status_code == 200:
    print("Conectado!")
else:
    print(f"Erro ao acessar o WMS. Código de erro: {response.status_code}")
