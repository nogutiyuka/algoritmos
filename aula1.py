class Pedir:
    def __init__(self):
        self.disc = ""
        self.ch = 0
        self.prof = ""

import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "algoritmos"
)

if(banco):
    print("Conectado com sucesso")
else:
    print("Erro na conexão")

cursor = banco.cursor()

sql = "INSERT INTO disciplinas VALUES (%s, %s, %s, %s)"
valores1 = (None, "ALGORITMOS", 160, "RAFAEL E AYSLAN")
valores2 = (None, "MATEMÁTICA DISCRETA E LÓGICA", 80, "AZUAITE")
valores3 = (None, "INGLÊS INSTRUMENTAL", 80, "VANESSA")

cursor.execute(sql, valores1)
cursor.execute(sql, valores2)
cursor.execute(sql, valores3)

a = Pedir()
a.disc = input("Informe o nome da disciplina: ")
a.ch = int(input("Informe a carga horária da disciplina: "))
a.prof = input("Informe o nome do professor da disciplina: ")

valoresUser = (None, a.disc, a.ch, a.prof)

"""resultados = cursor.fetchall()
for linha in resultados:
    print(linha)
    print("email: ", linha[3])
    print("nome: ", a.disc[0])
    print("ch: ", a.ch[1])
    print("professor: ", a.prof[2])

    print()

valoresUser = (sql, valoresUser)
cursor.execute(sql, valoresUser)"""

sql = "SELECT * FROM disciplinas ORDER BY nome"
cursor.execute(sql)
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)
    print("id: ", linha[0])
    print("nome: ", linha[1])
    print("idade: ", linha[2])
    print("email: ", linha[3])
    print()

banco.commit()

cursor.close()
banco.close()

