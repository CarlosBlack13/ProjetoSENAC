'''import sqlite3

conexao = sqlite3.connect("exemplo.db")
cursor = conexao.cursor()

cursor.execute('''
 CREATE TABLE IF NOT EXISTS usuario(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
        )
    ''')

conexao.close()'''