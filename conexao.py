import sqlite3
from sqlite3 import Error
import os

pastaApp=os.path.dirname(__file__)
nomeBanco=pastaApp + '\\banc.db'

def conexao():
    con=None
    try:
        con=sqlite3.connect(nomeBanco)
    except Error as ex:
        print(ex)

    return con

#select
def dql(query):
    vcon=conexao()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res



#delete,update,insert
def dml(query):
    try:
        vcon=conexao()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
    except Error as ex:
        print(ex)
