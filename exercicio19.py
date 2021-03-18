"""
Exercício 19
Nome: Praticando: Listas/For (Loop)
Objetivo: Praticar a criação e a leitura básica de listas com números e textos.
Dificuldade: Intermediário
1 - Crie uma lista com alguns números inseridos manualmente (não há necessidade do usuário inserí-los).
2 - Crie um for que varra cada elemento da lista e exiba-o no console.
3 - Declare um novo for que exiba apenas os números maiores que 3.
4 - Declare um outro for que exiba apenas os números pares.
5 - Exiba na tela a soma de todos os elementos da lista sem a utilização de funções extras.
6 - Exiba a soma de todos os elementos utilizando a função sum().
7 - Crie uma nova lista a partir de números digitados pelo usuário, faça com que o usuário insira 10 números, porém, 
utilize o 'for' para isso, em vez de declarar 10 vezes o input de entrada de informação, declare apenas UMA vez e 
faça com que ele seja executado 10 vezes.
A cada atualização da lista, exiba a quantidade de elementos que ela possui.
8 - Exiba apenas os três primeiros elementos da lista no console.
9 - Exiba apenas os três últimos elementos da lista no console.
10 - Declare uma nova lista vazia chamada 'nomes' e armazene 3 nomes digitados pelo usuário, ordene esses 
nomes por ordem alfabética e exiba-os na tela, um de cada vez.
"""
# Item 1
print("\n1 - Crie uma lista.")
lista = [1, 5, 2, 7, 9, 3, 58]
print(lista)

a = 0
lista2 = []
# Item 2

print("\n2 - Crie um for que varra cada elemento da lista e exiba-o no console.")
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")
print("\n")

# Item 3

print("3 - Declare um novo for que exiba apenas os números maiores que 3.")
for i in range(len(lista)):
    if lista[i] > 3:
        print(f"lista[{i}] = {lista[i]}")
print("\n")

# Item 4

print("4 - Declare um outro for que exiba apenas os números pares.")
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        print(f"lista[{i}] = {lista[i]}")
print("\n")

# Item 5

print("5 - Exiba na tela a soma de todos os elementos da lista sem a utilização de funções extras.")
for i in range(len(lista)):
    a += lista[i] 
print(f"\n{a}")


# Item 6

print("\n6 - Exiba a soma de todos os elementos utilizando a função sum().\n")
for i in range(len(lista)):
    print(sum(lista))
    break

# Item 7

print("\nDigite 10 números e a cada número novo na lista, exiba a quantidade de elementos que ela possui.")
def usuario(msg):
    num = int(input(msg))
    return num

for i in range (10):
    ent = usuario("Digite um número: ")
    lista2.append(ent)
    print(lista2)
b = []

# Item 8

print("\n8 - Exiba apenas os três primeiros elementos da lista no console.")
print(f"\nOs três primeiros valores da lista são: {lista2[0:3]}")

# Item 9

print("\n9 - Exiba apenas os três últimos elementos da lista no console.")
print(f"\nOs três últimos valores da lista são: {lista2[7:10]}")

# Item 10

print("\n10 - Digite 3 nomes , ordene esses nomes por ordem alfabética e exiba-os na tela, um de cada vez.")
e = []
def nome(msg):
    nomes = input(msg)
    return nomes

for i in range(3):
    en = nome(f"Digite o {i+1}° nome: ").title()
    e.append(en)
e.sort()
print("\n")
print(*e, sep='\n')