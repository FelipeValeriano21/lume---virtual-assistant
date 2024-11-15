import pandas as pd
import pyttsx3
from modules import comandos_respostas
comandos = comandos_respostas.comandos
respostas = comandos_respostas.respostas
import random
# Excluir um item especifico 
# Delete a specific item
# Listar lista de compras 
# Show the shopping list



def listarItens():
    df = pd.read_excel('devices/shopping_list/lista_de_compras.xlsx')
    itens_para_falar = ', '.join(df['produtos'].astype(str))
    engine = pyttsx3.init()
    engine.say(f"Os itens na lista são: {itens_para_falar}")
    engine.runAndWait()

# limpar a lista de compras    
# clean the shopping list
def limparLista():
    df = pd.read_excel('devices/shopping_list/lista_de_compras.xlsx')
    df_limpo = df.head(0) 
    df_limpo.to_excel('devices/shopping_list/lista_de_compras.xlsx', index=False)
    pyttsx3.speak("LImpeza de lista realizada com sucesso")


# adicionar um novo item   
# add a new item
def adicionarItem(item):

    df = pd.read_excel('devices/shopping_list/lista_de_compras.xlsx')
    if 'id' in df.columns:
        df = df.drop(columns=['id'])
    nova_linha = pd.DataFrame({'produtos': [item]})
    df = pd.concat([df, nova_linha], ignore_index=True)

    df.to_excel('devices/shopping_list/lista_de_compras.xlsx', index=False)
    print("Nova linha adicionada e arquivo salvo com sucesso!")
    pyttsx3.speak(item + "adicionado na lista com sucesso")
