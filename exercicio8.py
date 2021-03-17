"""
Exercício 8
Nome: Comparação de Números: Maior, Menor ou Igual
Objetivo: Receber dois números e exibir qual é maior, menor ou igual a quem.
Dificuldade: Principiante
1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Caso o {numero1} seja maior do que o {numero2}, exiba na tela: "O número {numero1} é maior do que o número {numero2}.";
3 - Caso contrário, se o {numero1} for menor, exiba: "O número {numero1} é menor que {numero2}.";
4 - Caso contrário, exiba: "O número {numero1} é igual ao número {numero2}.".
"""

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Degite o segundo número: "))

if numero_1 == numero_2:
    print(f"\nOs números {numero_1} e {numero_2} são iguais.")
elif numero_1 < numero_2:
    print(f"\nO número {numero_1} é menor que o número {numero_2}.")
else:
    print(f"\nO número {numero_1} é maior que o número {numero_2}.")