#Classic! Calcular a média do aluno com base em suas notas
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) /2

if media < 5:
    print(f'Média {media}, Aluno(a) reprovado(a)!')
elif media > 5 and media < 7:
    print(f'Média {media}, Aluno(a) está de recuperação!')
elif media > 7:
    print('Média {media}, Aluno(a) Aprovado(a)!')
