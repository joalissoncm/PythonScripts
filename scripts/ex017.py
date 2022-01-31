numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco',
          'seis', 'sete', 'oito','nove', 'dez')
while True:
    num = int(input('Digite um número de 0 até 10: '))
    if 0 <= num <= 10:
        break
    print(f'Inválido, tente Novamente. ', end='')
print(f'Você digitou o número {numeros[num]}')
