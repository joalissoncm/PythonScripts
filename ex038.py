print('Entrada - Rock & Code Party')

ano_atual = 2021
ano_nasc = int(input())

idade = ano_atual - ano_nasc

if idade >= 18:
    print('Entrada permitida.')
elif idade > 14:
    print('Entrada permitida desde que acompanhado(a).')
else:
    print('Entrada proibida.')
