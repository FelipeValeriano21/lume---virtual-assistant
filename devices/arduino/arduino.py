import serial
import time

# Configura a porta serial (ajuste o nome da porta conforme necessário)
arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela sua porta correta
time.sleep(2)  # Espera 2 segundos para a inicialização do Arduino

def ligar_leds():
    """Liga todos os LEDs com brilho máximo (255)."""
    arduino.write(b"LED1:255\n")
    arduino.write(b"LED2:255\n")
    arduino.write(b"LED3:255\n")
    print("LEDs ligados!")


def desligar_leds():
    arduino.write(b"LED1:0\n")
    arduino.write(b"LED2:0\n")
    arduino.write(b"LED3:0\n")
    print("LEDs desligados!")