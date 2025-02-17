README_CONTENT = """# 🗺️ WMS Image Request

Este script em Python permite requisitar imagens de mapas 📍 de um servidor WMS (Web Map Service) hospedado no GeoServer. Ele utiliza a biblioteca `requests` para realizar a requisição HTTP e `Pillow` para processar a imagem recebida.

## 🔍 Como funciona?

1. O código constrói uma URL contendo os parâmetros necessários para a requisição.
2. A requisição é enviada ao servidor WMS, que processa a solicitação e retorna a imagem.
3. A imagem do mapa dos municípios da Paraíba 🏙️ é baixada e salva no formato PNG.
4. Se tudo ocorrer bem, a imagem será salva localmente com o nome `PB_Municipios.png`.
5. Caso haja um erro, uma mensagem será exibida no console informando o problema ❌.

Este script pode ser facilmente modificado para obter imagens de diferentes camadas e regiões do mapa, bastando alterar os parâmetros da requisição.

🌍🚀
"""