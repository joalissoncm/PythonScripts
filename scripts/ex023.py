numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print(f'A lista tem {len(numeros)} elementos!')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numeros}')
if 5 in numeros:
    print('O número 5 está na lista!')
else:
    print('O número 5 não está na lista!')
