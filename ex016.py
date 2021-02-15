#Menu de opções
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
menu = 0

while menu != 5:
    menu = int(input('[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n'))
    if menu == 1:
        print(f'O resultado da soma é: {num1+num2}')
    elif menu == 2:
        print(f'O resultado da multiplicação é: {num1*num2}')
    elif menu == 3:
        if num1>num2:
            print(f'O maior número é: {num1})
        else:
            print(f'O maior número é: {num2})
    if menu == 4:
        print('Informe os númeors novos: ')
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
