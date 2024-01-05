from tkinter import *
from tkinter import messagebox

""" import os
import bancoNovoContato """

""" c=os.path.dirname(__file__)
nomeArquivo=c+'\\teste.txt'

def imprimirEsporte():
    ve=vesporte.get()
    if ve == 'Futebol':
        print('Esporte Futebol')
    elif ve == 'Basquete':
        print('Esporte Basquete')
    elif ve == 'Volei':
        print('Esporte Volei')
    elif ve == 'Tenis':
        print('Esporte Tenis')
    else:
        print('voce precisa selecionar um esporte') 

"""

#lb_esportes.pack()
#radioButton
"""
vesporte=StringVar()
#vcor=StringVar()
#radioButton
 rb_futebol=Radiobutton(app,text="Futebol",value="f",variable=vesporte)
rb_futebol.pack()

rb_basquete=Radiobutton(app,text="Basquete",value="b",variable=vesporte)
rb_basquete.pack()

rb_volei=Radiobutton(app,text="Volei",value="v",variable=vesporte)
rb_volei.pack()

rb_tenis=Radiobutton(app,text="Tenis",value="t",variable=vesporte)
rb_tenis.pack()

btn_esporte=Button(app,text="Esporte Selecionado",command=imprimirEsporte)
btn_esporte.pack()
 #option menu
listaEsportes=["Futebol","Volei","Basquete","Tenis"]

vesporte=StringVar()
vesporte.set(listaEsportes[0])
op_esportes=OptionMenu(app,vesporte,*listaEsportes)
op_esportes.pack()


"""



vmsg="teste de botao"

app = Tk()
app.title('Netshark Agenda')
app.geometry("800x450")
app.configure(background='#dde')

#################################teste
def mostrarMsg(tipomsg,msg):
    if(tipomsg ==1):
        messagebox.showinfo(title='Noticia',message=msg)
    elif(tipomsg==2):
        messagebox.showwarning(title='Cuidado',message=msg)
    elif(tipomsg==3):
        messagebox.showerror(title='Erro',message=msg)
    else:
        messagebox.showinfo(title='nada',message='nada digitado')
###############################teste
#lb_esportes=Label(app, text="Esportes",foreground="#000",anchor=W).place(x=10,y=10)

vnum_text=StringVar()

Label(app,text='Tipo de caixa (1),(2) ou (3)').pack()
tb_num=Entry(app,textvariable=vnum_text)
vnum_text.set(0)
tb_num.pack()
btn_msg=Button(app,text="Esporte Selecionado",command=lambda:mostrarMsg(vnum_text.get(),vmsg))
#btnmsg=Button(app,text='teste',command=lambda:mostrarMsg(vnum_text.get(),vmsg))
#btnmsg.pack()
btn_msg.pack()


app.mainloop()