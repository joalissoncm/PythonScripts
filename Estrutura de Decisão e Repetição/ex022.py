numeros = list()
while True:
    a = int(input('Digite um número: '))
    if a not in numeros:
        numeros.append(a)
        print('Valor adicionado!')
    else:
        print('Valor duplicado, não será adicionado!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort() #Função para colocar os números em ordem
print(f'Os números digitados foram: {numeros}')
