import requests
import pygame
import io
import pyttsx3

# Função para tocar uma música
def play_audio(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Carregar a música diretamente da resposta
            audio_data = io.BytesIO(response.content)  # Converte o conteúdo em um arquivo em memória

            pygame.mixer.init()
            pygame.mixer.music.load(audio_data) 
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            pygame.mixer.music.stop()  
        else:
            print("Falha ao baixar o áudio:", response.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o áudio: {e}")

def chamamusica(musica):
    url = f'https://deezerdevs-deezer.p.rapidapi.com/search?q={musica}'
    headers = {
        'X-RapidAPI-Key': '494f4935f7msh69281d3099327d6p1d498ejsn321e400c749f',
        'X-RapidAPI-Host': 'deezerdevs-deezer.p.rapidapi.com'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        data = response.json()

        if 'data' in data and data['data']:
            item = data['data'][0] 
            artista = item['artist']['name']
            titulo = item['title']
            preview = item['preview']
            pyttsx3.speak(f"Tocando a música {titulo} de {artista}")
            print(f"Artista: {artista}")
            print(f"Título: {titulo}")
            print(f"Preview: {preview}")
            return preview  
        else:
          
            pyttsx3.speak("Desculpe, não encontrei a música.")
            print("Nenhuma música encontrada para essa busca.")
            return None

    except requests.exceptions.RequestException as e:
        
        pyttsx3.speak("Desculpe, houve um erro ao buscar a música.")
        print(f"Erro ao fazer a requisição: {e}")
        return None
    except ValueError as e:
    
        pyttsx3.speak("Desculpe, houve um erro ao processar a resposta.")
        print(f"Erro ao processar a resposta: {e}")
        return None
