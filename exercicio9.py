"""
Exercício 9
Nome: Checando Múltiplos
Objetivo: Receber dois números e exibir se um é múltiplo do outro ou não.
Dificuldade: Principiante
1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Se o {numero1} for múltiplo do {numero2} exiba na tela: "O número {numero1} é múltiplo do número {numero2}.";
3 - Caso contrário, exiba na tela: "O número {numero1} não é múltiplo do número {numero2}.";
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 % numero2 == 0:
    print(f"\nO número {numero1} é múltiplo do número {numero2}.")
elif numero2 % numero1 == 0:
    print(f"\nO número {numero2} é múltiplo do número {numero1}.")
else:
    print(f"\nO número {numero1} não é múltiplo do número {numero2}.")