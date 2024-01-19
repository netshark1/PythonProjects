from tkinter import *
from tkinter import ttk

app=Tk()
app.geometry('600x400')
app.title('prgressBar')

def valBarra(m):
    cont=0
    etapas=m/100
    while cont < etapas:
        cont +=1
        i=0
        while i < 1000:
            i+=1
            vBarra.set(cont)
            app.update()

vBarra=DoubleVar()
vBarra.set(0)
pg=ttk.Progressbar(app,variable=vBarra,maximum=100)
pg.place(x=0,y=0,width=600,height=30)
btnp=Button(app,text='definir barra',command=lambda:valBarra(10000))
btnp.place(x=0,y=50)

app.mainloop()