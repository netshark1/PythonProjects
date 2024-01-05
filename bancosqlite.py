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

vcon = ConexaoBanco()

#cria tabela
vsql="CREATE TABLE tb_contatos(N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,T_NOMECONTATO TEXT(30),T_TELEFONECONTATO TEXT(30),T_EMAILCONTATO TEXT(30));"


def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print('Tabela Criada com sucesso!!!')
    except Error as ex:
        print(ex)


criarTabela(vcon,vsql)

vcon.close()