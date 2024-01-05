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
vnome=Entry(app)#entry
vnome.place(x=10,y=35,width=550,height=30)
texto2=Label(app, text='Telefone:',background="#dde",foreground="#000",anchor=W).place(x=10,y=70,width=180,height=30)
vtel=Entry(app)
vtel.place(x=10,y=95,width=250,height=30)
texto3=Label(app, text='Email:',background="#dde",foreground="#000",anchor=W).place(x=10,y=140,width=180,height=30)
vemail=Entry(app)
vemail.place(x=10,y=165,width=550,height=30)
texto4=Label(app, text='Obs:',background="#dde",foreground="#000",anchor=W).place(x=10,y=200,width=180,height=30)
vobs=Text(app)#text
vobs.place(x=10,y=245,width=400,height=150)
#Tkinter, Button Widget
def gravaDados():
    arquivo=open(nomeArquivo,'a')
    arquivo.write("Nome:%s"% vnome.get())
    arquivo.write("\nTelefone:%s"% vtel.get())
    arquivo.write("\nEmail:%s"%vemail.get())
    arquivo.write("\n Obs:%s"% vobs.get('1.0',END))
    arquivo.write('\n ')
    arquivo.close()
    #print('Obs:%s'% vobs.get())
#componentes entry e text


Button(app,text='imprimir',command=gravaDados).place(x=20,y=400,width=100,height=25)

app.mainloop()