"""
Exercício 13
Nome: Convertendo Celsius/Farenheit
Objetivo: Escrever duas funções de conversão, uma de graus celsius em farenheit e a outra que faça o contrário.
Dificuldade: Principiante
1 - Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit.
2 - Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão escolhida é realizada.
3 - Se C é a temperatura em Celsius e F em farenheit, as fórmulas de conversão são:
F = (9 * C / 5) + 32
C = 5 * (F - 32) / 9
"""

def c_para_f(celsius):
    F = (9 * celsius / 5) + 32
    return F
def f_para_c(fahrenheit):
    C = 5 * (fahrenheit - 32) / 9
    return C

ent = input("\nDigite 'C' para converter Celsius em Fahrenheit ou 'F' para converter Fahrenheit em Celsius: ").title()

if ent == 'C':
    cel = int(input("\nDigite o valor em Celsius que você seja converter para Fahrenheit: "))
    print(f"{cel}°C = {c_para_f(cel)}°F")

elif ent == 'F':
    fah = int(input("\nDigite o valor em Fahrenheit que você seja converter para Celsius: "))
    print(f"{fah}°F = {f_para_c(fah)}°C")
else:
    print("\nDigite C ou F")