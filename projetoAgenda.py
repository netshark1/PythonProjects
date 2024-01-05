import os
import sqlite3
from sqlite3 import Error

def ConexaoBanco():
    caminho= "agcont.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    

    return con


vcon= ConexaoBanco()

def query(conexao,sql):
    try:
        c= conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)

    finally:
        print('Operação realizada com sucesso')
        #conexao.close()

def consultar(conexao,sql):
    c= conexao.cursor()
    c.execute(sql)
    res= c.fetchall()
    conexao.commit()
    #conexao.close()
    return res



def menuPrincipal():
    #os.system('cls')
    print('1-Inserir Novo Registro')
    print('2-Deletar Registro')
    print('3-Atualizar Registro')
    print('4-Consultar Registro por Id')
    print('5-Consultar Registro por Nome')
    print('6-Sair')
    


def inserir():
     os.system('cls')
     vnome=input('digite o nome: ')
     vtel= input('digite o telefone: ')
     vemail=input('digite o email: ')
     vsql= "INSERT INTO contat(nome,telefone, email) VALUES('"+vnome+"','"+vtel+"','"+vemail+"')"
     query(vcon,vsql)



def deletar():
     os.system('cls')
     vid=input('Digite o Id do registro que deseja excluir: ')
     vsql="delete from contat where id='"+vid+"'"
     query(vcon,vsql)

def atualizar():
    os.system('cls')
    vid = input('digite o id do registro que voce deseja modificar: ')
    registro= consultar(vcon,"SELECT * FROM contat WHERE id='"+vid+"' ")
    respnome=registro[0][1]
    resptel=registro[0][2]
    respemail=registro[0][3]
    vnome= input('Digite o novo nome: ')
    vtel=input('Digite o novo telefone: ')
    vemail=input('Digite o novo Email')
    if(len(vnome) == 0):
        vnome=respnome
    if(len(vtel)==0):
        vtel=resptel
    if(len(vemail)==0):
        vemail=respemail

    vsql="UPDATE contat SET nome='"+vnome+"' ,telefone='"+vtel+"' ,email='"+vemail+"' WHERE id="+vid
    query(vcon,vsql)

def  consultarId():
    vsql="SELECT * FROM contat "
    resultado=consultar(vcon,vsql)
    vlimite=10
    vcont=0
    for r in resultado:
        print("id:{0:_>3} nome:{1:_<30} telefone:{2:_<14} email:{3:_>30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont >=vlimite):
            vcont=0
            os.system("pause")
            os.system("cls")

        print('Fim da Lista')
        os.system('pause')

    #query(vcon,vsql)

def   consultarNome():
            vnome = input('Digite o nome que deseja consultar: ')
            vsql="SELECT * FROM contat WHERE nome LIkE '%"+vnome+"%'"
            resultado=consultar(vcon,vsql)
            vlimite=10
            vcont=0
            for r in resultado:
                print("id:{0:_>3} nome:{1:_<30} telefone:{2:_<14} email:{3:_>30}".format(r[0],r[1],r[2],r[3]))
                vcont+=1
                if(vcont >=vlimite):
                    vcont=0
                    os.system("pause")
                    os.system("cls")
                    

                print('Fim da Lista')
                os.system('pause')


opc=0
while opc !=6:
    menuPrincipal()
    opc=int(input('Digite a opção desejada: '))
    if opc ==1:
        inserir()
      
    elif opc ==2:
         deletar()
      
    elif opc == 3:
        atualizar()
       
    elif opc == 4:
        consultarId()
     
    elif opc == 5:
          consultarNome()
        
    elif opc == 6 :
        os.system('cls')
        print('voce escolheu sair')
    else:
        os.system('cls')
        print('opcao invalida')
        os.system('pause')



vcon.close()

os.system('pause')

