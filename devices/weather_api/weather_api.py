import pyttsx3
import requests
import unicodedata

# Função para consultar a temperatura de uma cidade
def consultaTemperatura(cidade):
    cidade = limpaNome(cidade)
    parameters = {
        'key': 'jkqxgezgq3adgvx8hksv2k9wky7a6i48w3hb4vif',  
        'place_id': cidade
    }
    url = "https://www.meteosource.com/api/v1/free/point"
    
    try:
        response = requests.get(url, params=parameters)
        # Verifica se a resposta foi bem-sucedida
        response.raise_for_status()  # Vai gerar uma exceção se o status não for 200
        data = response.json()
        
        # Verifica se a chave 'current' e 'temperature' existem na resposta
        if 'current' in data and 'temperature' in data['current']:
            temperatura = data['current']['temperature']
            mensagem = f'A temperatura atual em {cidade} é {temperatura} °C.'
        else:
            mensagem = "Desculpe, local não encontrado ou dados inválidos."
    
    except requests.exceptions.RequestException as e:
        # Captura erros relacionados à requisição
        mensagem = f"Desculpe, não foi possível acessar a temperatura em {cidade}."
    except ValueError:
        # Captura erros ao tentar decodificar a resposta JSON
        mensagem = f"Desculpe, temperatura para {cidade} indisponível."
    
    return mensagem

# Função para limpar o nome da cidade (remover acentos e transformar em minúsculas)
def limpaNome(cidade):
    # Remover acentos
    cidade = unicodedata.normalize('NFKD', cidade).encode('ASCII', 'ignore').decode('ASCII')
    # Colocar tudo em minúsculo e substituir espaços por hífens
    cidade = cidade.lower().replace(" ", "-")
    return cidade
