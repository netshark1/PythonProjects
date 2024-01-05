from tkinter import *
import os
import banco

c=os.path.dirname(__file__)
nomeArquivo=c+'\\teste.txt'

app = Tk()
app.title('Netshark Agenda')
app.geometry("800x450")
app.configure(background='#dde')

#componentes entry,label e text
texto=Label(app, text='Nome:',background="#dde",foreground="#000",anchor=W).place(x=10,y=10,width=120,height=30)#label
tb_nome=Entry(app)#entry
tb_nome.place(x=10,y=35,width=550,height=30)
#telefone
texto2=Label(app, text='Telefone:',background="#dde",foreground="#000",anchor=W).place(x=10,y=70,width=180,height=30)
tb_tel=Entry(app)
tb_tel.place(x=10,y=95,width=250,height=30)
#email
texto3=Label(app, text='Email:',background="#dde",foreground="#000",anchor=W).place(x=10,y=140,width=180,height=30)
tb_email=Entry(app)
tb_email.place(x=10,y=165,width=550,height=30)
#obs
texto4=Label(app, text='Obs:',background="#dde",foreground="#000",anchor=W).place(x=10,y=200,width=180,height=30)
tb_obs=Text(app)#text
tb_obs.place(x=10,y=245,width=400,height=150)

#Tkinter, Button Widget
def gravaDados():
    if tb_nome.get() != "":
        vnome= tb_nome.get()
        vtel=tb_tel.get()
        vemail=tb_email.get()
        vobs=tb_obs.get("1.0",END)
        query="INSERT INTO contat(nome,telefone,email,obs) VALUES('"+vnome+"','"+vtel+"','"+vemail+"','"+vobs+"')"
        banco.dml(query)
        tb_nome.delete(0,END)
        tb_tel.delete(0,END)
        tb_email.delete(0,END)
        tb_obs.delete("1.0",END)
        print('Dados Gravados!!')
    else:
        print('Erro')

    os.system('cls')
    


Button(app,text='imprimir',command=gravaDados).place(x=20,y=400,width=100,height=25)

app.mainloop()