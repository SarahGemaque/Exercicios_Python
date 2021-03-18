"""
Exercício 16
Nome: Joguinho: Salão
Objetivo: Escrever uma função que funciona como um jogo, onde o usuário deve digitar as suas escolhas 
e o programa irá indicar o resultado das escolhas.
Dificuldade: Intermediário
Crie uma função principal chamada jogo() e execute as tarefas abaixo:
1 - O jogador irá entrar em um salão (informe isso a ele utilizando o comando print())
2 - Você deve perguntar se ele quer escolher entre a porta esquerda ou a direita
3 - Se a resposta for "esquerda" ou "e", exiba a mensagem:
- Você entrou na sala à esquerda, parece que não tem nada por aqui. Acho melhor você voltar correndo!
4 - Caso contrário, se a resposta for "direita" ou "d", exiba a mensagem:
- Excelente escolha! A sala à direita estava te esperando esse tempo todo! Que maravilhoso isso.
Pena que não tem nada aqui para você. :(
5 - Caso contrário, se a resposta não foi nenhum dos valores anteriores, exiba a mensagem abaixo e 
execute a função 'jogo()' novamente.
- Você não escolheu nenhuma das portas. Tente novamente.
"""

def jogo():
    print("\nVocê está em um salão, na sua frente existem duas portas, uma a direita e outra a esquerda.")
    a = input("Escolha um das portas com 'direita', 'd', 'esqueda' ou 'e': ").lower()

    if a == 'direita' or a == 'd':
        print("\nExcelente escolha! A sala à direita estava te esperando esse tempo todo! Que maravilhoso isso.")
        print("Pena que não tem nada aqui para você. :(")
    elif a == 'esquerda' or a == 'e':
        print("\nVocê entrou na sala à esquerda, parece que não tem nada por aqui.")
        print("Acho melhor você voltar correndo!")
    else:
        print("\nVocê não escolheu nenhuma das portas. Tente novamente.")

jogo()