from tkinter import*
from tkinter import messagebox


def mostarMsg(tipoMsg,msg):
    if(tipoMsg==1):
        messagebox.showinfo(title='Notícia',message=msg)
    elif(tipoMsg==2):
        messagebox.showwarning(title='Atenção',message=msg)
    elif(tipoMsg==3):
        messagebox.showerror(title='Erro',message=msg)
    else:
        messagebox.showinfo(title='nada apareceu',message='Não deu Certo')

vmsg='escolha uma msg'

def resetarTb():
    res=messagebox.askyesno('voce tem certeza?','confirma?')
    if(res==True):
        messagebox.showinfo('teste sim','teste sim')
    else:
        messagebox.showinfo('teste não','digitou não')

aplica= Tk()
aplica.title('aula messageBox')
aplica.geometry('800x600')
aplica.configure(background='#33ce20')

vnum=StringVar()
vnum.set(0)

num=Entry(aplica,textvariable=vnum)
num.place(x=30,y=90,width=30)
botao=Button(aplica,text='Escolha o Numero',command=lambda:mostarMsg(vmsg,vnum.get)).place(x=30,y=120,width=180)
btnReset=Button(aplica,text='resetar',command=resetarTb).place(x=30,y=150,width=120)

Label(aplica,text='escolha um numero(1,2 ou 3)',background='#33ce20',font=36).place(x=30,y=60)





aplica.mainloop()