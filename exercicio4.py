"""
Exercício 4
Nome: Data e Hora
Objetivo: Formatar a Data e Hora baseado em valores obtidos da biblioteca datetime e também valores informados pelo usuário.
Dificuldade: Intermediário
1 - Declare as variáveis para obter a data e a hora atual (dia, mês, ano, hora, minuto e segundo);
2 - Exiba essa informação para o usuário, devidamente formatada no formato "{DD}/{MM}/{AAAA} - {HH}h{MM}'{SS}".
3 - Peça para o usuário informar separadamente um dia, mês e ano e exiba no console
4 - Utilizando as informações digitadas pelo usuário, construa um objeto do tipo datetime.
5 - Exiba o a data fornecida, juntamente com o dia da semana correspondente, exemplo: {DD}/{MM}/{AAAA} - Dia da Semana: {data.weekday()}. OBS.: O dia da semana será exibido em inteiro, onde Segunda = 0 e Domingo é 6.
6 - Calcule a diferença entre as duas datas e exiba a quantidade em dias, exemplo: 'diferenca = data1 - data 2', print(diferenca.days)
Dica: Consulte a documentação em caso de dúvidas na manipulação do objeto datetime, como por exemplo a criação de um objeto datetime baseado em um dia, mês e ano personalizado.
Link para a Documentação do Datetime: https://docs.python.org/3/library/datetime.html
É possível criar um objeto do tipo datetime personalizado usando a seguinte declaração:
data_personalizada = datetime(ano, mes, dia, hora, minuto, segundo)
OBS.: Caso você tenha importado da seguinte maneira 'from datetime import datetime', a declaração acima funcionará.
Caso você tenha importado apenas com 'import datetime', você precisará declarar 'data_personalizada = datetime.datetime(ano, mes, dia, hora, minuto, segundo)'.
Você também pode criar uma data personalizada sem informar a hora, minuto e segundo, apenas informando os três primeiros parâmetros.
"""

from datetime import datetime
from datetime import date

# Item 1 e 2
data_1 = datetime.now()
print(f"\n{data_1.day}/{data_1.month}/{data_1.year} - {data_1.hour}h{data_1.minute}'{data_1.second}''\n")

# Item 3 e 4
dia, mes, ano = int(input("Digite o dia: ")), int(input("Digite o mês: ")), int(input("Digite o ano: "))

data = datetime(ano, mes, dia)
data_= datetime.date(data)

print(f"\n{data_}")

# Item 5

print(f"\n{data.day}/{data.month}/{data.year} - Dia da Semana: {data.weekday()}")

# Item 6

diferenca = data_1 - data
print(f"\nA diferença entre as datas é de {diferenca.days} dias.\n")