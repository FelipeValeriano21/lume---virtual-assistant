#importando bibliotecas
#from arduino import arduino
import pyttsx3
import speech_recognition as sr
from playsound import playsound
import random
import datetime
import webbrowser as wb
import numpy as np
import librosa
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import locale
import pygame
import time
import requests
import os
sns.set()
import requests
from pydub import AudioSegment
from pydub.playback import play
import requests
from io import BytesIO
import datetime
from modules import comandos_respostas
comandos = comandos_respostas.comandos
respostas = comandos_respostas.respostas

from devices.time_date import time_date

from devices.weather_api import weather_api

from devices.song_api import song_api

from devices.shopping_list import shopping_list

from devices.arduino import arduino

meu_nome = 'lume'



# Função para falar
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200) 
    engine.setProperty('volume', 1) 
    engine.say(audio)
    engine.runAndWait()

playsound('assets/sounds/Alexa_Sound.mp3')


# Função para gravar audio
def listen_microphone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        audio = microfone.listen(source)
        with open('assets/sounds/recordings/speech.wav', 'wb') as f:
            f.write(audio.get_wav_data())
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    return frase

playing = False
mode_control = False
print('Lume iniciando...')
print('Tudo pronto')
pyttsx3.speak(f"Bem-vindo! Meu nome é lume e sou uma assistente virtual")
pyttsx3.speak(f"Para começar que tal perguntar: lume O que você faz?")


# Loop assitente
while (1):
    result = listen_microphone()

    if meu_nome in result:
        result = str(result.split(meu_nome + ' ')[1])
        result = result.lower()
        print('-------------------Acionou a assistente!-------------------')
        print('-------------------Após o processamento: ', result)

        if result in comandos[0]:
            pyttsx3.speak('Até agora minhas funções são: ' + respostas[0])

        if result in comandos[1]:
            pyttsx3.speak('Agora são ' + time_date.definirHora())

        if result in comandos[2]:
            pyttsx3.speak('Hoje é dia ')
            pyttsx3.speak(time_date.definirData())

        if result in comandos[3]:
            playsound('assets/sounds/Alexa_Sound.mp3')
            pyttsx3.speak('Diga uma musica para eu tocar ')
            musica = listen_microphone()
            playsound('assets/sounds/Alexa_Sound.mp3')
            url = song_api.chamamusica(musica)
            song_api.play_audio(url)

        if result in comandos[4]:
            playsound('assets/sounds/Alexa_Sound.mp3')
            pyttsx3.speak('Diga a cidade que gostaria de saber a temperatura')
            cidade = listen_microphone()
            playsound('assets/sounds/Alexa_Sound.mp3')
            whtemperatura = weather_api.consultaTemperatura(cidade)
            pyttsx3.speak(whtemperatura)
            

        # Lista de Compras
        if result in comandos[5]:
            playsound('Alexa_Sound.mp3')
            speak('Pode falar!')
            result = listen_microphone()
            anotacao = open('anotacao.txt', mode='a+', encoding='utf-8')
            anotacao.write(result + '\n')
            anotacao.close()
            speak(''.join(random.sample(respostas[1], k=1)))
            speak('Deseja que eu leia os lembretes?')
            result = listen_microphone()
            if result == 'sim' or result == 'pode ler':
                with open('anotacao.txt') as file_source:
                    lines = file_source.readlines()
                    for line in lines:
                        speak(line)
            else:
                speak('Ok!')

        if result in comandos[6]:
           playsound('assets/sounds/Alexa_Sound.mp3')
           pyttsx3.speak('listar, adicionar ou limpar')
           elemento = listen_microphone()
    
           match elemento:
             case "listar":
                   shopping_list.listarItens()  
             case "adicionar": 
                    pyttsx3.speak("Diga um produto para ser adicionado")
                    item = listen_microphone()
                    speak(''.join(random.sample(respostas[1], k=1)))
                    shopping_list.adicionarItem(item)
             case "limpar":
                   shopping_list.limparLista()      
             case "excluir elemento":
                   shopping_list.excluirItem()     
             case _:
                    pyttsx3.speak('Opção não encontrada')


        if result in comandos[7]:
            pyttsx3.speak('Ligando os leds')
            arduino.ligar_leds()

        if result in comandos[8]:
            pyttsx3.speak('desLigando os leds')
            arduino.desligar_leds()

        if result == 'encerrar':
            playsound('assets/sounds/Alexa_Sound.mp3')
            pyttsx3.speak(''.join(random.sample(respostas[4], k = 1)))
            break
        else:
          print("TESTE")

       
            

playing = False
mode_control = False
playsound('assets/sounds/Alexa_Sound.mp3')
print('\nPronto para começar!')
