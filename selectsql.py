import sqlite3
from sqlite3 import Error

#cria conexao
def  ConectaBanco():
    caminho='agenda.db'
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)

    return con

vcon = ConectaBanco()

def consulta(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado=c.fetchall()
    return resultado

vsql="Select * From tb_contatos"
res=consulta(vcon,vsql)
for r in res:
    print(r)

