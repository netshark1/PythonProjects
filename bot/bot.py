import openpyxl
import webbrowser
from time import sleep
from urllib.parse import quote
#import pywhatkit
import pyautogui
import os


webbrowser.open('https://web.whatsapp.com')
sleep(30)
workbook=openpyxl.load_workbook('C:\\Users\\HelioTome\\Documents\\PythonProjects\\bot\\clientes.xlsx')
pagina=workbook['Sheet1']
for linha in pagina.iter_rows(min_row=2):
    nome=linha[0].value
    telefone=linha[1].value
    vencimento=linha[2].value
    mensagem=f'Ola {nome}, seu boleto venceu no dia{vencimento}'
    linkMsg=f'https://web.whatsapp.com/send?phone={telefone} & {quote(mensagem)}'
    #linkMsg=pywhatkit.sendwhatmsg(f'{nome}, {vencimento},{mensagem}',9,14)
    webbrowser.open(linkMsg)
    sleep(10)
    try:
        seta=pyautogui.locateCenterOnScreen('C:\\Users\\HelioTome\\Documents\\PythonProjects\\bot\\seta.png')
        sleep(2)
        pyautogui.click(seta[0],seta[1])
        sleep(2)
        pyautogui.hotkey('ctrl','w')
        sleep(2)
    except:
        print(f'Não foi possível enviar mensagem para {nome}')
        with open('erros.csv','a',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone},{vencimento}')


""" 
PRECISO AUTOMATIZAR MINHAS MENSAGENS P/ MEUS CLIENTES GOSTARIA DE SABER VALORES, 
E GOSTARIA QUE ENTRASSEM EM CONTATO COMIGO P/ EXPLICAR MELHOR, QUERO PODER MANDAR 
MENSAGENS DE COBRANÇA EM DETERMINADO DIA COM CLIENTES COM VENCIMENTO DIFERENTE
"""
