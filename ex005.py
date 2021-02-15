# Programa ler um número e retorna o seu dobro trilho e raiz quadrada
num = int(input('Digite um número: '))
d = num * 2
t = num * 3
r = num ** (1/2)
print('O dobro de {} é {}. O triplo é {} \nE a raiz quadrada é {:.2f}'.format(num, d, t, r))
