from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

def clicaFut():
    print('futebol'+' '+vFutbol.get())

def clicaVolei():
    print('volei'+' '+ vVolei.get())

def clicaBask():
    print('basquete'+' '+vBasket.get())


def mostraSenha():
    print('senha digitada:' + vsenha.get())

pastaApp=os.path.dirname(__file__)

app= Tk()
app.title('webshark')
app.geometry('600x700')

vFutbol=StringVar()
vVolei=StringVar()
vBasket=StringVar()


#elementi imagem

imageLogo=PhotoImage(file=pastaApp+'\\images.png')

fr_quadro_1= Frame(app,borderwidth=1,relief='solid').place(x=10,y=10,width=350,height=250)
labelLogo=Label(fr_quadro_1,image=imageLogo).place(x=12,y=15)

#checkbutton

cbF=Checkbutton(fr_quadro_1,text='futebol',variable=vFutbol,onvalue='sim',offvalue='nao',command=clicaFut).place(x=15,y=190)
cbV=Checkbutton(fr_quadro_1,text='volei',variable=vFutbol,onvalue='sim',offvalue='nao',command=clicaVolei).place(x=95,y=190)
cbB=Checkbutton(fr_quadro_1,text='Basquete',variable=vFutbol,onvalue='sim',offvalue='nao',command=clicaBask).place(x=145,y=190)

#password

vsenha=StringVar()
pSenha=Entry(app,textvariable=vsenha,show='*').place(x=10,y=270)
btnMS=Button(app,text='mostrar a senha',command=mostraSenha).place(x=10,y=295)

#combobox
def ImprimeEsporte():
    print('esporte escolhido: '+ cbEsportes.get())

cbEsportes=StringVar()
listaEsportes=['futebol','volei','basquete']
lBEsporte=Label(app,text='Esportes').place(x=10,y=355)
cbEsportes=ttk.Combobox(app,values=listaEsportes)
cbEsportes.set('futebol')
cbEsportes.place(x=10,y=375)
btncb=Button(app,text='imprime esporte',command=ImprimeEsporte).place(x=10,y=395)

#scale
#nao faz parte da subbiblioteca ttk

def valorEscala():
    print('o valor da escala é: '+ str(esca.get()))

#esca=StringVar()
lbValor=Label(app,text='Valor do Scale').place(x=10,y=435)
esca=Scale(app,from_=0,to=50,orient=HORIZONTAL).place(x=10,y=455)
esca.set(25)
btnValor=Button(app,text='imprima o valor da escala',command=valorEscala).place(x=10,y=495)


app.mainloop()