# Programa recebe dois números inteiros e mostra qual é o maior ou se são valores iguais
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'O primeiro número é maior, {num1}!')
elif num2 > num1:
    print(f'O segundo número é maior, {num2}!')
else:
    print('Os números são iguais!')
