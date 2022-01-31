num = [4, 1, 7, 6, 2]
num[1] = 9          #Coloca o 9 na posição 1
num.append(3)       #Adiciona mais um elemento
num.sort()          #Coloca os elementos em ordem, colocando reverse=True fica ao contrário
num.insert(4, 8)    #Insere elemento na posição, por exemplo, 8 na posição 4
if 8 in num:
    num.remove(8)   #Remove o elemento selecionado
else:
    print('O número 8 não foi encontrado')
print(num)
print(f'Esta lista tem {len(num)} elementos')
