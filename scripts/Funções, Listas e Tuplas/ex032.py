def numprimo():
    num = int(input('Digite um número: '))
    num2 = num % 2
    if num2 == 0:
        return f'O número {num} é PAR'
    else:
        return f'O número {num} é ÍMPAR'


print(numprimo())
