import requests
from io import BytesIO
from PIL import Image

def request_wms_image():
    GEO_URL = "http://localhost:8080/geoserver/Lucas_Rickelme/wms"
    
    params = {
        "service": "WMS",
        "version": "1.1.1",
        "request": "GetMap",
        "layers": "Lucas_Rickelme:PB_Municipios_2023",
        "styles": "",
        "bbox": "-38.7656034,-8.3029551,-34.7930865,-6.0259119",
        "width": "1920",
        "height": "1080",
        "srs": "EPSG:4674",
        "format": "image/png",
        "scale": "136000"
    }
    
    try:
        response = requests.get(GEO_URL, params=params)
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save("PB_Municipios.png", "PNG")
            print("Mapa salvo com o nome 'PB_Municipios.png'")
        else:
            print(f"Erro na requisição: {response.status_code} - {response.reason}")
    except Exception as e:
        print("Erro ao requisitar a imagem do WMS:", e)

request_wms_image()
