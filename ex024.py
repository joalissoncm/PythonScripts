# Programa recebe o nome é o peso e mostra quantas pessoas foram cadastradas
# e mostre quem tem o maior e o menor peso.
pessoal = []
principal = []
maior = menor = 0
while True:
    pessoal.append(str(input('Nome: ')))
    pessoal.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = pessoal[1]
    else:
        if pessoal[1] > maior:
            maior = pessoal[1]
        if pessoal[1] < menor:
            menor = pessoal[1]
    principal.append(pessoal[:])
    pessoal.clear()
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
       break
print(f'{len(principal)} pessoas foram cadastradas!')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
