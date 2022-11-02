#estrutura de dados é como a gente consegue representar dados na memória do computador, ou seja, variaveis

#registros = estruturas

#Vetor é homogênio e Registro é heterogênio

#Registros são os dados de uma linha de uma tabela de um banco de dados

#Nomes de classes em Java e Python começa com letra maiúscula
def sexo(num):
    if(num == 1):
        num = True
    elif(num == 2):
        num = False
    else:
        num = False
    return num


def mensagem(a):
    if (a.sexo == True):
        print("\n")
        print(f"Nome: {a.nome}\nIdade: {a.idade} anos de idade\nE-email: {a.email}\nSexo: Masculino\nData de nascimento: {a.dataNascimento.dia}/{a.dataNascimento.mes}/{a.dataNascimento.ano}")
    elif(a.sexo == False):
        print("\n")
        print(f"Nome: {a.nome}\nIdade: {a.idade} anos de idade\nE-email: {a.email}\nSexo: Feminino\nData de nascimento: {a.dataNascimento.dia}/{a.dataNascimento.mes}/{a.dataNascimento.ano}")


class Data:
    def __init__(self):
        self.dia = 0
        self.mes = 0
        self.ano = 0

class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.email = ""
        self.sexo = False  # False = feminino     True = masculino
        self.dataNascimento = Data()

class Professor:
    def __init__(self):
        self.nome = ""
        self.idade = 0
        self.salario = 0.0
        self.dataNascimento = Data()

"""a = Aluno() #Aluno é um tipo de dado que criamos, um registro.
a.nome = "Maria da Silva"
a.idade = 22
a.email = input("Informe seu e-mail: ")
a.sexo = int(input("Digite 1 para Masculino e 2 para Feminino: "))
a.sexo = sexo(a.sexo)
"""
b = Aluno()

b.nome = input("Informe seu nome: ")
b.idade = int(input("Informe sua idade: "))
b.email = input("Informe seu e-mail: ")
b.sexo = int(input("Digite 1 para Masculino e 2 para Feminino: "))
b.sexo = sexo(b.sexo)
b.dataNascimento.dia = int(input("Informe o dia do seu nascimento: "))
b.dataNascimento.mes = int(input("Informe o mês do seu nascimento: "))
b.dataNascimento.ano = int(input("Informe o ano do seu nascimento: "))

mensagem(b)



"""c = Data()

c.dia = int(input("Informe o dia: "))
c.mes = int(input("Informe o mês: "))
c.ano = int(input("Informe o ano: "))

print(f"A data de hoje é: {c.dia}/{c.mes}/{c.ano}")"""

#Classe: é um modelo para um conjunto de coisas, essas coisas são os objetos. Ou seja, uma classe é um modelo para esses objetos. Uma classes é um molde, um template, uma generalização para um grupo de coisas.

#Objeto é uma instância de uma classe. Uma instância de uma classe nada mais é você ter uma variavel daquele tipo da classe. É a variável daquela classe.

