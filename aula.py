"""
# PARTE 1
Criar função chamada criarVetor que recebe um número inteiro por parâmetro representando o 
tamanho de um vetor. A função deve criar o vetor, preencher com valores aleatórios entre 1 e 200 e retornar o vetor.
No algoritmo principal, solicite o tamanho do vetor para o usuário e crie o vetor utilizando a função.

# PARTE 2
Crie um procedimento chamado exibirVetor para exiba na tela o vetor recebido por parâmetro.

# PARTE 3
Crie uma função chamada somaImpares que calcule e retorne a soma de todos os números ímpares de um vetor recebido por parâmetro.
No algoritmo principal, apresente a soma na tela.

# PARTE 4
Implemente um procedimento chamado busca que recebe por parâmetro um número informado pelo usuário. 
O procedimento deve, usando a busca sequencial, exibir uma mensagem na tela dizendo se o número 
está ou não presente em um vetor também recebido por parâmetro.

# PARTE 5
Implemente uma função chamada ordenar que recebe dois parâmetros: um vetor de números inteiros e o 
nome de um algoritmo de ordenação (bolha, inserção ou seleção). Ordene e retorne o vetor recebido 
de acordo com o parâmetro de ordenação. Obs: o código de ordenação está no Moodle (tópico Aulas)
"""
import funcoes

num = int(input("Informe o tamanho do vetor: "))
vetor = funcoes.criarVetor(num)
funcoes.exibirVetor(vetor)
soma = funcoes.somaImpares(vetor)
print(soma)

buscar = int(input("Informe o número que você queira buscar: "))

funcoes.busca(buscar, vetor)

metodo = input("Informe o nome do método de ordenação escolhido (bolha, inserção ou seleção).\nOBS: Escrever com todas as letras minúsculas: ").lower()

funcoes.ordenar(vetor, metodo)


