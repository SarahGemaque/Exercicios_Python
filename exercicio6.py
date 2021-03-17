"""
Exercício 6
Nome: Catapulta
Objetivo: Receber o número de baterias e duração da bateria e calcular a quantidade de pedras que a catapulta irá soltar.
Dificuldade: Principiante
1 - Uma catapulta lançou 300 pedras em 5 baterias de 15 minutos, cada.
2 - Quantas pedras ela lançaria em 8 baterias de 7 minutos, cada?
3 - Crie um programa que receba os valores base para que a aplicação funcione de forma que, se alterarmos o número 
de bateriais e a duração de cada bateria, o programa funcione sem precisar de mais modificações.
"""
catapulta = 300 / (5*15)

baterias = int(input("Digite o número de baterias: "))
duracao = int(input("Digite a duração das baterias: "))

quantidade_pedras = baterias * duracao * catapulta

print(f"\nA catapulta lançou {quantidade_pedras:.0f} pedras em {baterias} baterias de {duracao} minutos.")