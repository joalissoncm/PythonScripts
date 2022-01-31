numeros = []
posmax = []
posmin = []
for cont in range(0, 5):
    numeros.append(int(input('Digite um número: ')))
for pos, valor in enumerate(numeros):
    if valor == max(numeros):
        posmax.append(pos)
    if valor == min(numeros):
        posmin.append(pos)
print(f'Os numeros digitados foram: {numeros}')
print(f'O maior valor foi {max(numeros)}, nas posições {posmax}')
print(f'O menor valor foi {min(numeros)}, nas posições {posmin}')
