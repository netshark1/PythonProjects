import sqlite3
from sqlite3 import Error


#cria conexao
def ConexaoBanco():
    caminho="agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)

    return con

vcon= ConexaoBanco()
i= input('digite o nome que deseja deletar: ')

vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO='"+i+"' "

def deletarDados(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        
    except Error as ex:
        print(ex)
    finally:
        print('dados deletados com sucesso!')


deletarDados(vcon,vsql)

    