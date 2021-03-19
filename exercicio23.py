"""
Exercício 23
Nome: Pedra, Papel e Tesoura
Objetivo: Criar um jogo de pedra, papel e tesoura, jogador versus computador.
Dificuldade: Intermediário
1 - Crie um programa que receba uma jogada do usuário (pedra, papel ou tesoura).
Exiba a mensagem: "Você jogou {}.", onde '{}' é a jogada do usuário.
2 - Faça com que seu jogo rode infinitamente, a menos que o usuário digite "sair".
3 - Caso o usuário digite "pedra, papel ou tesoura", prossiga com o jogo, caso ele digite "sair", encerre 
o jogo e caso ele digite qualquer outra coisa, pergunte a jogada novamente.
4 - Faça com que o programa ignore se o usuário digitou Pedra, PEDRA, ou pEdRa, ambos devem ser entendidos como "pedra".
5 - Gere uma jogada aleatória para o computador.
Exiba a mensagem: "Computador jogou {}.", onde '{}' é a jogada do computador.
6 - Exiba o resultado da jogada.
Pedra quebra Tesoura.
Tesoura corta Papel.
Papel embrulha Pedra.
7 - Caso o jogador tenha ganhado, exiba: "Você ganhou.", caso contrário, exiba: "Você perdeu.".
8 - Você também deverá criar um placar para o jogo, onde cada jogada que o jogador vencer, adicione 1 ponto 
ao placar do jogador e cada jogada que o computador vencer, adicione um ponto ao placar do computador.
Ao término da execução do programa (quando o jogador digitar "sair"), exiba a quantidade de rodas, a quantidade 
de pontos de cada um, se o jogador venceu, perdeu ou se deu empate.
"""
import random
cond = True
comp = ['pedra', 'papel', 'tesoura']
placar_jog = 0
placar_comp = 0
placar_emp = 0
cont = 0

def vezes (num):
    if num == 1:
        return 'vez'
    else:
        return 'vezes'

while(cond):
    ent = input("\nEscolha pedra, papel ou tesoura: ").lower()
    cont += 1
    
    if(ent == 'pedra' or ent == 'papel' or ent == 'tesoura'):
        print(f"\nVocê jogou {ent}.")
        sorteio = random.choice(comp)
        print(f"O computador jogou {sorteio}.")

        if (ent == 'pedra' and sorteio == 'tesoura') or (ent == 'tesoura' and sorteio == 'pedra'):
            print("\nPedra quebra Tesoura.")
            if ent == 'pedra':
                print("\nVocê ganhou.")
                placar_jog += 1
            else:
                print("\nVocê perdeu.")
                placar_comp += 1
        elif (ent == 'tesoura' and sorteio == 'papel') or (ent == 'papel' and sorteio == 'tesoura'):
            print("\nTesoura corta Papel.")
            if ent == 'tesoura':
                print("\nVocê ganhou.")
                placar_jog += 1
            else:
                print("\nVocê perdeu.")
                placar_comp += 1
        elif (ent == 'papel' and sorteio == 'pedra') or (ent == 'pedra' and sorteio == 'papel'):
            print("\nPapel embrulha Pedra.")
            if ent == 'papel':
                print("\nVocê ganhou.")
                placar_jog += 1
            else:
                print("\nVocê perdeu.")
                placar_comp += 1
        elif ent == sorteio:
            print("\nSão iguais.")
            print("Deu empate.")
            placar_emp += 1
    elif ent == 'sair':
        cont -= 1
        print(f"\nO jogo rodou {cont} {vezes(cont)}, o jogador ganhou {placar_jog} {vezes(placar_jog)}, o computador ganhou {placar_comp} {vezes(placar_comp)}, o jogo empatou {placar_emp} {vezes(placar_emp)}.")
        break
    else:
        continue
if placar_jog > placar_comp:
	print("\nVocê venceu.")
elif placar_comp > placar_jog:
	print("\nVocê perdeu.")
else:
	print("\nO jogo terminou em empate.")
   
        

