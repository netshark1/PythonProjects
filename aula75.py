from tkinter import *

app=Tk()
app.title('spinbox')
app.geometry('600x400')

def mostrarValores():
    
        mostra=sb_valores.get()
        print('valor capturado: '+ str(mostra.get()))
   
sb_valores= Spinbox(app,values=(1,2,3,4,5,6))
sb_valores.pack()
btn_valores=Button(app,text='mostrar valores',command=mostrarValores)
btn_valores.pack()


app.mainloop()