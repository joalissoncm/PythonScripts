numeros = (int(input('Digite o 1° numero: ')),
       int(input('Digite o 2° número: ')),
       int(input('Digite o 3° número: ')),
       int(input('Digite o 4° número: ')))
print(f'Os números digitados foram: {numeros}')
print(f'O número 9 foi digitado: {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado')
