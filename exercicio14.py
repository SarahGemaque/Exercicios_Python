"""
Exercício 14
Nome: Média Escolar
Objetivo: Escrever uma aplicação utilizando funções que calcule a média de um aluno.
Dificuldade: Intermediário
1 - Um professor, muito legal, fez 3 provas durante um semestre mas só vai levar em conta as duas notas 
mais altas para calcular a média.
2 - Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média
 com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.
"""

def entrada(msg):
    ent = int(input(msg))
    return ent

def comparar_maior(a,b):
    if a < b:
        return b
    elif b < a:
        return a
    elif a == b:
        return a

def comparar_menor(a,b):
    if a < b:
        return a
    elif b < a:
        return b
    elif a == b: 
        return a        

nota1 = entrada("\nDigite a primeira nota: ")
nota2 = entrada("Digite a segunda nota: ")
nota3 = entrada("Digite a terceira nota: ")

maior = comparar_maior(nota1,nota2)
maior = comparar_maior(maior, nota3)

menor = comparar_menor(nota1,nota2)
menor = comparar_menor(menor, nota3)

media_total = (nota1 + nota2 + nota3)/3
media_2notas = (nota1 + nota2 + nota3 - menor)/2

print(f"\nA média das 3 provas seria {media_total:.1f}")
print(f"\nA média com as duas notas mais altas é {media_2notas:.1f}")

if maior != menor:
    print(f"\nA nota mais alta foi {maior} e a nota mais baixa foi {menor}")
elif maior == menor:
    print(f"\nTodas as notas são iguais a {maior}")