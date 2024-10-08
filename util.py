import sqlite3

def obter_conexão():
    conexao= sqlite3.connect('dados.db')
    return conexao