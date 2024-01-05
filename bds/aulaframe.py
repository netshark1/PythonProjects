from tkinter import *
from tkinter import messagebox


def mostrarMsg():
    messagebox.showinfo('mensagem','aula de frame')


aplica=Tk()
aplica.geometry('600x480')
aplica.configure(background='#fcfcfc')

Label(aplica,text='Aula de frame',background='#cd45ef',foreground='#000').place(x=30,y=60)
caixa=Frame(aplica,width=300,background='#c0c0c0', height=120,borderwidth=1,relief='solid').place()

botao=Button(caixa,text='clicar para mostrar',command=mostrarMsg).place()
Label(caixa,text='estou dentro do frame',foreground='#000').place()
aplica.mainloop()
