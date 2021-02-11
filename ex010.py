#Programa deve ler um nome completo e mostrar o nome com letras maiúsculas,
#minúsculas, quantas letras no total e quantas letras tem o primeiro nome
nome = str(input('Digite um nome: ')).strip()
print('Em letras maiúsculas:{}'.format(nome.upper()))
print('Em letras minúsculas:{}'.format(nome.lower()))
print('O nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
