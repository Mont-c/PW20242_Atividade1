#Comando para criar a tabela 'produto' se ela não existir
SQL_CRIAR_TABELA = """
CREATE TABLE IF NOT EXISTS produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT NOT NULL,
    estoque INTEGER NOT NULL,
    preco REAL NOT NULL,
    categoria TEXT NOT NULL
);
"""

#Comando para inserir um novo produto na tabela 'produto'
SQL_INSERIR = """
INSERT INTO produto (nome, descricao, estoque, preco, categoria)
VALUES (?, ?, ?, ?, ?);
"""

#Comando para excluir um produto da tabela 'produto' usando o id
SQL_EXCLUIR = """
DELETE FROM produto WHERE id = ?;
"""
