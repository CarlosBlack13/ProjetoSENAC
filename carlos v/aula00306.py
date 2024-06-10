#realiizamos a importação da biblíoteca SQLite
import sqlite3

#abrimos a conexão e atribuimos ela a uma variável
conexao = sqlite3.connect("exemplo.db")
cursor = conexao.cursor()

cursor.execute("INSERT INTO usuario (nom, idade) VALURES(?, ?)",("Carlos", 18))
cursor.execute("INSERT INTO usuario (nom, idade) VALURES(?, ?)",("Caio", 16))
cursor.execute("INSERT INTO usuario (nom, idade) VALURES(?, ?)",("Camilly", 15))

conexao.commit()

conexao.close()