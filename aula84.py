from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

def mp(mm):
    return mm/0.352777


pastaArq= os.path.dirname(__file__)

def criarPdf():
    try:
        cnv=canvas.Canvas(pastaArq+'\\doc.pdf',pagesize=A4)
        cnv.drawString(mp(30),mp(270),'bem vindo ao meu primeiro arquivo2')
        cnv.circle(mp(100),mp(100),mp(100))
        cnv.drawImage(pastaArq+'\\images.png',mp(30),mp(200))
        
        cnv.save()
    except:
        messagebox.showinfo(title='ERRO',message='Erro ao Criar PDF')

app=Tk()
app.title('ReportLab')
app.geometry('600x400')


btnCp=Button(app,text='criar pdf',command=criarPdf)
btnCp.pack(side=LEFT,padx=10)

app.mainloop()