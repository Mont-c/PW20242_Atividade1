from datetime import datetime
import sqlite3


NOME_PASTA_HTML = "html/"
NOME_PASTA_CADASTROS = ""

def ler_html(nome_arquivo: str) -> str:
    caminho_arquivo_html = f"{NOME_PASTA_HTML}{nome_arquivo}.html"
    with open(caminho_arquivo_html, "r", encoding="utf-8") as arquivo:
        conteudo_html = arquivo.read
    return conteudo_html

def salvar_cadastro(nome, descricao, produto, preco, categoria):
    agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"{NOME_PASTA_CADASTROS}cadastro_{agora}.txt"
    conteudo = f"Nome: {nome}\nDescricao: {descricao}\nProduto: {produto}\nPreco: {preco}\nCategoria: {categoria}"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)

def obter_conexao():
    return sqlite3.connect("dados.db")