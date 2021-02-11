# Calcular o desconto de 5%

preco = int(input('Informe o valor do produto: R$ '))
desc = (preco * 5 / 100)
print('O valor do produto com desconto é: {:.2f}'.format((preco - desc)))
