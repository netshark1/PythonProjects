from tkinter import *

app=Tk()
app.title('listbox')
app.geometry('600x400')


def imprimeEsporte():
    print('escolhido: '+ lbEsp.get(ACTIVE))


listaEsportes=['Futebol','Volei','Basquete']

lbEsp=Listbox(app)

for esportes in listaEsportes:
    lbEsp.insert(END,esportes)
    
lbEsp.pack()

btnEsp=Button(app,text='imprime Esporte',command=imprimeEsporte).place(x=10,y=10) 

def insereEsp():
    lbEsp.insert(eEsp.get(listaEsportes))


eEsp=Entry(app)
eEsp.pack()
btnIE=Button(app,text='inserir Esporte',command=insereEsp)
btnIE.place(x=10,y=50)

app.mainloop()