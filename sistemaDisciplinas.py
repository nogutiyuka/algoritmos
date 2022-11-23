import mysql.connector

#conectar no banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="algoritmos"
)

if(banco):
    print("Conectado com sucesso")
else:
    print("Erro na conexão")

class Disciplina:
    def __init__(self):
        self.codigo = None
        self.disc = ""
        self.carga = 0
        self.prof = ""
        self.chr = 0.0

def salvar (disciplina):
    cursor = banco.cursor()
    sql = "INSERT INTO disciplinas(nome, ch, professor, chr) VALUES (%s, %s, %s, %s)"

    valores = (disciplina.disc, disciplina.carga, disciplina.prof, disciplina.chr)
    cursor.execute(sql, valores)
    banco.commit()

    arq = open("arquivo.txt", "a")
    arq.write("{};{};{};{};{}\n".format(disciplina.codigo, disciplina.disc, disciplina.carga, disciplina.prof, disciplina.chr))
    arq.close()


def lerDados():
    cursor = banco.cursor()
    sql = "SELECT * FROM disciplinas;"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    print("Total de linhas retornadas: ", cursor.rowcount)

    for linha in resultados:
        print(linha)
        print("Código: ", linha[0])
        print("Disciplina: ", linha[1])
        print("Carga Horária: ", linha[2])
        print("Professor: ", linha[3])
        print("CHR: ", linha[4])
    
def usuario(a):
    a.disc = input("Informe o nome da disciplina: ")
    a.carga = int(input("Informe a carga horária da disciplina: "))
    a.prof = input("Informe o nome do(a) professor(a): ")
    a.chr = (a.carga * 50)/60
    return a

b = Disciplina()
a = usuario(b)
salvar(a)

c = usuario(b)
salvar(c)

lerDados()
