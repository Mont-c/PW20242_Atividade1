import sqlite3
from sql.produto_sql import SQL_CRIAR_TABELA, SQL_INSERIR
from models.produto_model import Produto


#função Criar tabela
def criar_tabela(conexao):
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_CRIAR_TABELA)
        conexao.commit()


#funçâo Inserir

def inserir(conexao, produto: Produto):
    with conexao:
        cursor = conexao.cursor()
        cursor.execute(SQL_INSERIR, (produto.nome, produto.descricao, produto.estoque, produto.preco, produto.categoria))
        conexao.commit()

#função Obter todos

def obter_todos(conexao):
    with conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, descricao, estoque, preco, categoria FROM produto")
        resultados = cursor.fetchall()

        produtos = []
        for linha in resultados:
            produto = Produto(
                id=linha[0],
                nome=linha[1],
                descricao=linha[2],
                estoque=linha[3],
                preco=linha[4],
                categoria=linha[5],
            )
            produtos.append(produto)

        return produtos