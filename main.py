import tkinter as tk
from threading import Thread
import pyttsx3
import speech_recognition as sr
from playsound import playsound
import random
from devices.time_date import time_date
from devices.weather_api import weather_api
from devices.song_api import song_api
from devices.shopping_list import shopping_list
from modules import comandos_respostas
from tkinter import PhotoImage
from PIL import Image, ImageTk
from devices.arduino import arduino


# Inicializando comandos e respostas
comandos = comandos_respostas.comandos
respostas = comandos_respostas.respostas

meu_nome = 'lume'

# Função para falar
def speak(audio):
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('volume', 1)
    engine.say(audio)
    engine.runAndWait()

# Função para gravar áudio
def listen_microphone():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source, duration=0.8)
        print('Ouvindo:')
        label_status.config(text="Ouvindo...")  
        audio = microfone.listen(source)
    try:
        frase = microfone.recognize_google(audio, language='pt-BR')
        print('Você disse: ' + frase)
    except sr.UnknownValueError:
        frase = ''
        print('Não entendi')
    label_status.config(text="Lume falando...")  
    return frase


def assistant():
    print('Lume iniciando...')
    speak("Bem-vindo! Meu nome é Lume e sou uma assistente virtual.")
    speak("Para começar, que tal perguntar: Lume, o que você faz?")
    
    while True:
        result = listen_microphone()
        if meu_nome in result:
            result = result.lower().replace(f"{meu_nome} ", "")
            print(f"Comando recebido: {result}")

            if result in comandos[0]:
                speak(respostas[0])
            elif result in comandos[1]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                button_icon4.config(bg="lime")
                speak('Agora são ' + time_date.definirHora())
                button_icon4.config(bg="white")
            elif result in comandos[2]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                button_icon6.config(bg="lime")
                speak('Hoje é dia ' + time_date.definirData())
                button_icon6.config(bg="white")
            elif result in comandos[3]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                button_icon1.config(bg="lime")
                speak('Diga uma música para eu tocar')
                musica = listen_microphone()
                url = song_api.chamamusica(musica)
                song_api.play_audio(url)
                button_icon1.config(bg="white")
            elif result in comandos[4]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                button_icon2.config(bg="lime")
                speak('Diga a cidade para saber a temperatura')
                cidade = listen_microphone()
                whtemperatura = weather_api.consultaTemperatura(cidade)
                speak(whtemperatura)
                button_icon2.config(bg="white")
            elif result in comandos[6]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                button_icon3.config(bg="lime")
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
                button_icon3.config(bg="white")
            elif result in comandos[7]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                button_icon5.config(bg="lime")
                pyttsx3.speak('Ligando os leds')
                arduino.ligar_leds()
                button_icon5.config(bg="white")

            elif result in comandos[8]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                button_icon5.config(bg="lime")
                pyttsx3.speak('desligando os leds')
                arduino.desligar_leds()
                button_icon5.config(bg="white")


            elif result in comandos[9]:
                playsound('assets/sounds/Alexa_Sound.mp3')
                pyttsx3.speak(''.join(random.sample(respostas[4], k=1)))
                root.quit() 
                break
            else:
                speak("Desculpe, não entendi o comando.")


def on_button_click():
    label_greeting.config(text="LUME iniciada")
    Thread(target=assistant).start()  

# Funções para os ícones
def icon_function_1():
    speak("Você clicou no ícone 1.")

def icon_function_2():
    speak("Você clicou no ícone 2.")

def icon_function_3():
    speak("Você clicou no ícone 3.")

def icon_function_4():
    speak("Você clicou no ícone 4.")

def icon_function_5():
    speak("Você clicou no ícone 5.")

def icon_function_6():
    speak("Você clicou no ícone 6.")


root = tk.Tk()
root.title("Assistente Virtual - Lume")
root.geometry("350x600") 
root.configure(bg="white")


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)  
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)
root.grid_columnconfigure(2, weight=1)

frame_lume = tk.Frame(root, bg="white")
frame_lume.grid(row=0, column=0, rowspan=2, padx=10, pady=20, sticky="nw")

image = Image.open("assets/images/lume.png")

resized_image = image.resize((50, 50))

new_image = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(frame_lume, image=new_image, bg="white")
image_label.grid(row=0, column=0)

label_status = tk.Label(root, text="Lume falando...", font=("Arial", 14), bg="white")
label_status.grid(row=1, column=1, pady=20)

label_greeting = tk.Label(root, text="LUME - Assistente Virtual", font=("Arial", 12), bg="white")
label_greeting.grid(row=0, column=1, pady=20) 

button = tk.Button(root, text="Iniciar Assistente", font=("Arial", 12), command=on_button_click)
button.grid(row=2, column=0, columnspan=3, pady=10) 


icon1 = Image.open("assets/images/song.png")
icon2 = Image.open("assets/images/temperatura.png")
icon3 = Image.open("assets/images/list.png")

icon4 = Image.open("assets/images/clock.png")  # Exemplo de ícone de relógio
icon5 = Image.open("assets/images/lamp.png")  # Exemplo de ícone de calendário
icon6 = Image.open("assets/images/date.png")  # Exemplo de ícone de lista de compras

# Redimensionando as imagens
icon1_resized = icon1.resize((40, 40))
icon2_resized = icon2.resize((40, 40))
icon3_resized = icon3.resize((40, 40))
icon4_resized = icon4.resize((40, 40))
icon5_resized = icon5.resize((40, 40))
icon6_resized = icon6.resize((40, 40))

# Converter para PhotoImage
icon1_photo = ImageTk.PhotoImage(icon1_resized)
icon2_photo = ImageTk.PhotoImage(icon2_resized)
icon3_photo = ImageTk.PhotoImage(icon3_resized)
icon4_photo = ImageTk.PhotoImage(icon4_resized)
icon5_photo = ImageTk.PhotoImage(icon5_resized)
icon6_photo = ImageTk.PhotoImage(icon6_resized)


button_icon1 = tk.Button(root, image=icon1_photo, command=icon_function_1, bg="white", relief="flat")
button_icon1.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

button_icon2 = tk.Button(root, image=icon2_photo, command=icon_function_2, bg="white", relief="flat")
button_icon2.grid(row=3, column=1, padx=20, pady=10, sticky="nsew")

button_icon3 = tk.Button(root, image=icon3_photo, command=icon_function_3, bg="white", relief="flat")
button_icon3.grid(row=3, column=2, padx=20, pady=10, sticky="nsew")

button_icon4 = tk.Button(root, image=icon4_photo, command=icon_function_4, bg="white", relief="flat")
button_icon4.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")

button_icon5 = tk.Button(root, image=icon5_photo, command=icon_function_5, bg="white", relief="flat")
button_icon5.grid(row=4, column=1, padx=20, pady=10, sticky="nsew")

button_icon6 = tk.Button(root, image=icon6_photo, command=icon_function_6, bg="white", relief="flat")
button_icon6.grid(row=4, column=2, padx=20, pady=10, sticky="nsew")

root.mainloop()
