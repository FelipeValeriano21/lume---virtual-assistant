import locale
import datetime

# Função para dizer a data de hoje
# Funtion to tell the date today

def definirData(): 
  locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
  date = datetime.date.today().strftime('%d de %B meu amigo')
  return date

def definirHora():
    hour = datetime.datetime.now().strftime('%H:%M')
    return hour