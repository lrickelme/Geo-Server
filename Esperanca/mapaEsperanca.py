import requests
from io import BytesIO
from PIL import Image

def request_wms_image(layer_name):
    WMS_URL = "http://localhost:8080/geoserver/wms"
    
    params = {
        "service": "WMS",
        "version": "1.3.0",
        "request": "GetMap",
        "layers": f"{layer_name}:PB_Municipios_2023",
        "styles": "",
        "crs": "EPSG:4326",
        "bbox": "-7.22,-36.06,-6.82,-35.66",
        "width": "800",
        "height": "600",
        "format": "image/png",
        "scale": "136000",
        "transparent": "true"
    }
    
    try:
        response = requests.get(WMS_URL, params=params)
        
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            image.save("esperanca_wms.png", "PNG")
            print("Imagem salva em: esperanca_wms.png")
        else:
            print(f"Erro na requisição: {response.status_code} - {response.reason}")
    except Exception as e:
        print("Erro ao requisitar a imagem do WMS:", e)


request_wms_image("Lucas_Rickelme")