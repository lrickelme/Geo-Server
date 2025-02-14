import requests

GEO_URL = "http://localhost:8080/geoserver/Lucas_Rickelme/wms"
PARAMETROS = {
    "service": "WMS",
    "version": "1.1.1",
    "request": "GetMap",
    "layers": "Lucas_Rickelme:PB_Municipios_2023",
    "styles": "",
    "bbox": "-35.8597,-7.02278,-35.8497,-7.01278",
    "width": "1920",
    "height": "1080",
    "srs": "EPSG:4674",
    "format": "image/png",
    "scale": "136000"
}

response = requests.get(GEO_URL, params=PARAMETROS)

if response.status_code == 200:
    with open("PB_Municipios.png", "wb") as file:
        file.write(response.content)
    print("Mapa salvo como 'Esperanca.png'")
else:
    print(f"Erro ao obter a imagem WMS.")
