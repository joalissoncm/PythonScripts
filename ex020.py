#Recebendo valores numa lista
valores = list()
for cont in range(0, 5):    #For para guardar os númeors na lista
    valores.append(int(input('Digite um número: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
