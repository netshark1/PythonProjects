from tkinter import *
from tkinter import ttk
import os

app=Tk()
app.title('abas e notebook')
app.geometry('600x400')


ntb=ttk.Notebook(app)
tb1=Frame(ntb)
tb2=Frame(ntb)
tb3=Frame(ntb)
ntb.place(x=0,y=0,width=600,height=200)

ntb.add(tb1,text='aba1')
ntb.add(tb2,text='aba2')
ntb.add(tb3,text='aba3')

lb1=Label(tb1,text='estamos na aba 1')
lb1.pack()

lb2=Label(tb2,text='estamos na aba 2')
lb2.pack()

lb3=Label(tb3,text='estamos na aba 3')
lb3.pack()

app.mainloop()