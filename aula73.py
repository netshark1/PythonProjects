from tkinter import *


app=Tk()
app.geometry('600x400')
app.title('labelFrame')

lb=LabelFrame(app,text='Labelframe Esportes',borderwidth=1,relief='solid').place(x=10,y=10,width=300,height=100)
labelF=Label(lb,text='fusca').place(x=25,y=25)
labelu=Label(lb,text='up').place(x=25,y=45)
labelFox=Label(lb,text='fox').place(x=25,y=65)
labelp=Label(lb,text='passat').place(x=95,y=25)
labelT=Label(lb,text='tempra').place(x=95,y=45)

app.mainloop()