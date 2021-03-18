"""
Exercício 12
Nome: Praticando Funções
Objetivo: Escrever diversas funções para reaproveitar trechos de código
Dificuldade: Intermediário
Escreva um código de modo que exiba o valor do x digitado pelo usuário e que seja
substituído nas funções.
1 - Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).
2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável
de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine
o custo de produção de 100 peças.
3 - Crie uma função que receba 2 números e retorne o maior valor.
4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.
5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da
soma de f(9) + g(2). Depois crie um código que retorne o valor da soma das duas funções
com números digitados pelo usuário.
6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1.
Qual é o valor da função composta g(f(3))? Depois crie um código que retorne o valor da
soma das duas funções com números digitados pelo usuário.
7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6.
Exiba 10 números sorteados utilizando a mesma função criada.
Números aleatórios: random.randint(inicio, fim)
"""

def entrada(msg):
    ent = int(input(msg))
    return ent

# Item 1

# Problema
print("\n1. Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).\n")
# Resolução
def valor(num):
    f_x = 3*num - 2
    return f_x

x = entrada("Digite o valor de x: ")
outro = entrada("Digite outro valor para x: ")

print(f"\nO valor da soma de f({x}) e f({outro}) é igual a {valor(x) + valor(outro)}")

# Item 2

# Problema
print("\n2. Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine o custo de produção das peças.\n")
#Resolução
def preco(p):
    return 30 + 2*p
    
pecas = entrada("Digite o número de peças: ")
print(f"\nO valor a pagar para {pecas} peças unitárias é: {preco(pecas)}")

# Item 3

# Problema
print("\n3. Digite 2 números e descubra o número de maior valor.\n")
# Resolução
def verificar_maior(numero1,numero2):
    if numero1 < numero2:
        return numero2
    else:
        return numero1

numero1 = entrada("Digite o primeiro número: ")
numero2 = entrada("Digite o segundo número: ")

maior = verificar_maior(numero1,numero2)
print(f"Entre {numero1} e {numero2}, o maior valor é: {verificar_maior(numero1,numero2)}.")


# Item 4

# Problema
print("\n4. Digite 3 números e descubra o número de maior valor\n")
#Resolução
numero1 = entrada("Digite o primeiro número: ")
numero2 = entrada("Digite o segundo número: ")
numero3 = entrada("Digite o terceiro número: ")
maior = verificar_maior(numero1,numero2)
maior = verificar_maior(maior,numero3)

print(f"Entre {numero1}, {numero2} e {numero3}, o maior valor é: {maior}.")

# Item 5 

# Problema
print("\n5. Dadas as funções f(x) = x – 5 e g(x) = 3x + 1. Digite um x para f(x) e um x para g(x) e descubra a soma das duas funções.\n")
# Resolção
def funcao(f,g):
    f_x = f - 5
    g_x = 3*g + 1
    return f_x + g_x

x = entrada("Digite o valor de x para f(x): ")
y = entrada("Digite o valor de x para g(x): ")
print(f"\nA soma de f({x}) e g({y}) é igual a {funcao(x,y)}")

# Item 6
 
# Problema
print("\n6. Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1. Descubra o valor da função composta g(f(x)) e a soma das duas funções.\n")
# Resolução
def gef(a):
    g_f_x = 5*(a-4) + 1
    return g_f_x

def soma(a):
    f_x = a - 4
    g_x = 5*a + 1
    return f_x + g_x

a = entrada("Digite o valor de x para f(x): ")

print(f"\nA soma de f({a}) e g({a}) é igual a {soma(a)}")
print(f"\nA função composta g(f({a})) é {gef(a)}")


# Item 7

# Problema
print("\n7. Sorteie 10 números, de 1 até o número que você precisa\n")
# Resolução
import random
def dado(tamanho):
    return random.randint(1, tamanho)

tamanho = entrada("Digite o valor máximo do sorteio: ")
print("\n")

for i in range (10):
    print (f"O numero {i} sorteado é {dado(tamanho)}")