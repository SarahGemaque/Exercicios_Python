"""
Exercício 7
Nome: Arredondando para Múltiplos
Objetivo: Receber dois números e arredondar o primeiro número para o número mais próximo do múltiplo do segundo número.
Dificuldade: Principiante
1 - Receba dois números, o primeiro na variável 'numero' e o segundo na variável 'multiplo'.
2 - Arredonde para baixo o valor do primeiro número levando em consideração que o resultado deve ser múltiplo do segundo número.
Exemplo:
Supondo que o primeiro número seja 72 e o segundo número seja 10, o resultado será 70.
Se o primeiro número for 97 e o segundo número for 10, o resultado será 90.
"""

numero = int(input("Digite um número: "))
multiplo = int(input("Digite um número que será o multiplo: "))

div = numero//multiplo

for i in range (div+1):
    i *= multiplo

print(f"\nO número {numero} arrendondado para baixo para ser múltiplo de {multiplo} é: {i}")