# Classic! Ler um número inteiro e mostrar a tabuada

num = int(input('Digite um número: '))
for a in range(1, 11):
    print('{} x {} = {}'.format(num, a, num * a))
