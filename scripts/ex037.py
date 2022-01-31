print('Bem-vindo(a)! Para abrir uma conta corrente responda às seguintes perguntas: ')

p1 = input('Você tem em mãos o documento de identidade, sim ou não?')
p2 = input('Você tem em mãos um comprovante de residência, sim ou não? ')

if p1 == 'não' or p2 == 'não':
    print('Sinto muito, você não tem os documentos necessários para a abertura de conta corrente.')
else:
    print('Certo. Vamos prosseguir com a abertura da sua conta corrente.')
