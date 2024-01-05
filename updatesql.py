import sqlite3
from sqlite3 import Error

#criaBD
def ConectaBanco():
    caminho='agenda.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)

    return con
#u=input('digite o nome que deseja atualizar')

vcon = ConectaBanco()

vsql= "UPDATE  tb_contatos SET T_NOMECONTATO='Tomé' where N_IDCONTATO='1'"

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)

    finally:
        print('dados atualizados com sucesso!!!')

atualizar(vcon, vsql)

vcon.close()
    
