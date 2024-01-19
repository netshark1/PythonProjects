from tkinter import *
from tkinter import ttk

app=Tk()
app.title('treeView')
app.geometry('600x300')

listaNomes=[['0','joao','33444545'],['1','jose','33444545'],['2','Maria','33444545']]

#for lista in listaNomes:

tv=ttk.Treeview(app,columns=('id','nome','telefone'),show='headings')
tv.column('id',minwidth=0,width=50)
tv.column('nome',minwidth=0,width=100)
tv.column('telefone',minwidth=0,width=100)
tv.heading('id',text='ID')
tv.heading('nome',text='Nome')
tv.heading('telefone',text='Telefone')

for (id,nome,telefone) in listaNomes:
    tv.insert('','end',values=(id,nome,telefone))

tv.place(x=10,y=10,width=450)
app.mainloop()