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

nome= input('digite o nome: ')
telefone= input('digite o telefone: ')
email= input('digite o email: ')

vcon = ConexaoBanco()

vsql= "INSERT INTO  tb_contatos (T_NOMECONTATO ,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES ('"+nome+"','"+telefone+"','"+email+"')"
def inserirDados(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Dados inseridos com sucesso!!")
    except Error as ex:
        print(ex)

inserirDados(vcon,vsql)

vcon.close()