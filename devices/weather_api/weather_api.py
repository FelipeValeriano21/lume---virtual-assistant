
import pyttsx3
import requests
# Função para consultar a temperatura de uma cidade
# Function to get the temperature from a city

def consultaTemperatura(cidade):
    cidade = limpaNome(cidade)
    parameters = {
        'key': 'jkqxgezgq3adgvx8hksv2k9wky7a6i48w3hb4vif',  
        'place_id': cidade
    }
    url = "https://www.meteosource.com/api/v1/free/point"
    response = requests.get(url, params=parameters)
    data = response.json()

    mensagem = 'A temperatura atual em' + cidade + ' é {} ° Celsius.'.format(data['current']['temperature'])

    return mensagem 
   




import unicodedata

def limpaNome(cidade):
    # Remover acentos
    cidade = unicodedata.normalize('NFKD', cidade).encode('ASCII', 'ignore').decode('ASCII')
    # Colocar tudo em minúsculo e substituir espaços por hífens
    cidade = cidade.lower().replace(" ", "-")
    return cidade

