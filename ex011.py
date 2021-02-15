#Programa calcula se o número é par ou ímpar
num = int(input('Digite um número: '))
num2 = num % 2
if num2 == 0:
    print('O número é {} PAR'.format(num))
else:
    print('O número é {} ÍMPAR'.format(num))
