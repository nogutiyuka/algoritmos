import random

def criarVetor(num):
    vetor = [0] * num
    for b in range(0, num):
        vetor[b] = random.randint(1, 200)
    return vetor

def exibirVetor(vetor):
    for a in range(0, len(vetor)):
        print(f"Vetor[{a}] = {vetor[a]}")

def somaImpares(vetor):
    soma = 0
    for i in range(0, len(vetor)):
        if (vetor[i] % 2 != 0):
            soma += vetor[i]
    return soma

def busca(buscar, vetor):
    achar = False
    for d in range(0, len(vetor)):
        if (vetor[d] == buscar):
            achar = True
            break
    if (achar == True):
        print(f"O número {buscar} foi encotrado! ")
    else:
        print(f"O número {buscar} não foi encontrado!")

def ordenar(vetor, metodo):
    if (metodo == 'bolha'):
        for i in range(0, len(vetor)-1):
            for j in range(0, len(vetor)-1):
                if(vetor[j] > vetor[j+1]):
                    temp = vetor[j]
                    vetor[j] = vetor[j+1]
                    vetor[j+1] = temp
        print()
        for i in range(0, len(vetor)):
            print(vetor[i], " ", end="")

    elif (metodo == 'inserção'):
        for i in range(0, len(vetor)):
            chave = vetor[i]
            j = i-1
            while((j >= 0) and (vetor[j] > chave)):
                vetor[j+1] = vetor[j]
                j = j - 1
            vetor[j+1] = chave
        print()
        for i in range(0, len(vetor)):
            print(vetor[i], " ", end="")

    elif (metodo == 'seleção'):
        for i in range(0, len(vetor) - 1):
            i_menor = i
            for j in range(i+1, len(vetor)):
                if(vetor[j] < vetor[i_menor]):
                    i_menor = j
            menor = vetor[i_menor]
            vetor[i_menor] = vetor[i]
            vetor[i] = menor
        print()

        for i in range(0, len(vetor)):
            print(vetor[i], " ", end="")
    else:
        print("O método escolhido não foi reconhecido! ")
