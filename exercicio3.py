  
"""
Exercício 3
Nome: Input de Informações
Objetivo: Receber dados do usuário, trabalhar com os valores e exibir para o usuário.
Dificuldade: Principiante
1 - Crie um programa que receba do usuário seu nome, idade e gênero;
2 - Exiba na tela seguinte mensagem: "Olá, {nome}, você possui {idade} anos de idade e é do gênero {genero}. Já pensou no que você fará no seu aniversário de {idade + 1} anos?".
"""

nome, idade, genero = input("Digite o seu nome: "), int(input("Digite a sua idade: ")), input("Digite o seu gênero: ")
print(f"\nOlá, {nome.title()}, você possui {idade} anos de idade e é do gênero {genero.lower()}.")
print(f"Já pensou no que você fará no seu aniversário de {idade + 1} anos?")