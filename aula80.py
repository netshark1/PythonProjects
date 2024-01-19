from tkinter import *
from tkinter import ttk
from tkinter import messagebox

app=Tk()
app.title('treeView')
app.geometry('850x450')


#listaNomes=[['0','joao','33444545'],['1','jose','33444545'],['2','Maria','33444545']]

def inserir():
    if vid.get()=='' or vNom.get()=='' or vTel.get()=='':
        messagebox.showinfo(title='ERRO!!',message='digite todos os dados')
        return
    tv.insert('','end',values=(vid.get(),vNom.get(),vTel.get()))
    vid.delete(0,END)
    vNom.delete(0,END)
    vTel.delete(0,END)
    vid.focus()
    


def deletar():
    print()


def obter():
    print()


btnInserir=Button(app,text='inserir dado',command=inserir)
btnInserir.grid(column=0,row=6,sticky='w')
btnDeletar=Button(app,text='deletar dado',command=deletar)
btnDeletar.grid(column=1,row=6,sticky='w')
btnObterr=Button(app,text='obter dado',command=obter)
btnObterr.grid(column=2,row=6,sticky='w')


tv=ttk.Treeview(app,columns=('id','nome','telefone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=200)
tv.column('telefone',minwidth=0,width=400)
tv.heading('id',text='ID')
tv.heading('nome',text='Nome')
tv.heading('telefone',text='Telefone')
tv.grid(column=0,row=3,rowspan=3,pady=0,sticky='w')


lbId=Label(app,text='ID')#,anchor='w')
lbId.grid(column=0,row=0,sticky='w')
vid=Entry(app)
vid.grid(column=0,row=1,sticky='w')

lbNome=Label(app,text='Nome')#,anchor='w')
lbNome.grid(column=1,row=0,sticky='w')
vNom=Entry(app)
vNom.grid(column=1,row=1,sticky='w')


lbTel=Label(app,text='Telefone')
lbTel.grid(column=2,row=0,sticky='w')
vTel=Entry(app)
vTel.grid(column=2,row=1,sticky='w')




""" for (id,nome,telefone) in listaNomes:
    tv.insert('','end',values=(id,nome,telefone)) """


#tv.insert('','end',values=(id,nome,telefone))

#tv.place(x=10,y=10,width=450)
app.mainloop()