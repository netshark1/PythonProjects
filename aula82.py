from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import conexao

###############################FUNÇÔES##################################################
def popular():
    tv.delete(*tv.get_children())
    vquery='SELECT * FROM cont order by id'
    linhas=conexao.dql(vquery)
    for i in linhas:
        tv.insert('','end',values=i)

def inserir():
    if vNOME.get()=='' or vTELEFONE.get()=='':
        messagebox.showinfo(title='ERRO!!!',message='digite todos os dados')

        return
    try:
        vquery="INSERT INTO cont (nome,telefone) VALUES ('"+vNOME.get()+"','"+vTELEFONE.get()+"') "
        conexao.dml(vquery)
    except:
        messagebox.showinfo(title='ERRO!!!',message='ERRO AO INSERIR DADOS!!!')

        return
    popular()
    vNOME.delete(0,END)
    vTELEFONE.delete(0,END)
    vNOME.focus()
    

def deletar():
    vID=-1
    itemSelecionado=tv.selection()[0]
    valores=tv.item(itemSelecionado,'values')
    vID=valores[0]
    try:
        vquery="DELETE FROM cont WHERE id="+vID
        conexao.dml(vquery)
    except:
        messagebox.showinfo(title='ERRO!!!',message='ERRO AO DELETAR ARQUIVO!')
        return
    tv.delete(itemSelecionado)

def pesquisar():
    tv.delete(*tv.get_children())
    vquery="SELECT * FROM cont WHERE nome LIKE '%"+vPESQUISAR.get()+"%'ORDER BY id"
    linhas=conexao.dql(vquery)
    for i in linhas:
        tv.insert('','end',values=i)
        


#########################ABRE APP############################################
app=Tk()
app.title('treeView')
app.geometry('850x450')


#################################quadro######################################3
quadrogrid=LabelFrame(app,text='contatos')
quadrogrid.pack(fill='both',expand='yes',padx=10,pady=10)


tv=ttk.Treeview(quadrogrid,columns=('ID','NOME','TELEFONE'),show='headings')
tv.column('ID',minwidth=0,width=50)
tv.column('NOME',minwidth=0,width=200)
tv.column('TELEFONE',minwidth=0,width=400)
tv.heading('ID',text='ID')
tv.heading('NOME',text='NOME')
tv.heading('TELEFONE',text='TELEFONE')
tv.pack()
popular()

##################################LABEIS########################################

lbId=Label(quadrogrid,text='ID')
lbId.place(x=40,y=250)

lbNOME=Label(quadrogrid,text='NOME')
lbNOME.place(x=190,y=250)

lbTELEFONE=Label(quadrogrid,text='TELEFONE')
lbTELEFONE.place(x=350,y=250)

#########################ENTRYS##############################################
vID=Entry(quadrogrid)
vID.place(x=40,y=280)

vNOME=Entry(quadrogrid)
vNOME.place(x=190,y=280)

vTELEFONE=Entry(quadrogrid)
vTELEFONE.place(x=350,y=280)

vPESQUISAR=Entry(quadrogrid)
vPESQUISAR.place(x=40,y=350)

####################BOTÕES######################################################
btnInserir=Button(quadrogrid,text='inserir',command=inserir)
btnInserir.place(x=40,y=310)

btnDeletar=Button(quadrogrid,text='Deletar',command=deletar)
btnDeletar.place(x=190,y=310)

btnObter=Button(quadrogrid,text='Pesquisar',command=pesquisar)
btnObter.place(x=100,y=350)

app.mainloop() 