from tkinter import *
from tkinter import ttk

app=Tk()
app.geometry('600x300')
app.title('Grid4')

lbCanal=ttk.Label(app,text='curso1')
lbCanal.place(x=10,y=20)
lbNome=ttk.Label(app,text='digite seu nome')
lbNome.place(x=10,y=40)
lbIdade=ttk.Label(app,text='digite sua idade')
lbIdade.place(x=10,y=60)

eNome=Entry(app)
eIdade=Entry(app)

eNome.place(x=10,y=120)
eIdade.place(x=10,y=80)


btnC=Button(app,text='clica aqui')
btnC.place(x=10,y=100)

lbCanal.grid(column=0,row=0)

app.mainloop()