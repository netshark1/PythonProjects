from tkinter import *
import os
#import bancoNovoContato 

pastaApp=os.path.dirname(__file__)
abrej=pastaApp+"\\contato.py"

def semComando():
    print('sem comando')


def novoContato():
    exec(open(abrej).read())

app = Tk()
app.title('Netshark Agenda')
app.geometry("800x450")
app.configure(background='#dde')

barraDeMenus=Menu(app)
menuContatos= Menu(barraDeMenus,tearoff=0)
menuContatos.add_command(label="Novo",command=novoContato)
menuContatos.add_command(label="Pesquisar",command=semComando)
menuContatos.add_command(label="Deletar",command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar",command=app.quit)
barraDeMenus.add_cascade(label="Contatos",menu=menuContatos)
app.config(menu=barraDeMenus)

#menu Manutenção

menuManutencao=Menu(barraDeMenus,tearoff=0)
menuManutencao.add_command(label="Banco de Dados",command=semComando)
barraDeMenus.add_cascade(label="Manutenção",menu=menuManutencao)

#menu sobre

menuSobre=Menu(barraDeMenus,tearoff=0)
menuSobre.add_command(label="Netshark",command=semComando)
barraDeMenus.add_cascade(label="Sobre",menu=menuSobre)

#radio button

app.mainloop()