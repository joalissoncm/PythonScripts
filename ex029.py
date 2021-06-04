def area(a, b):
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area}m²')


largura = float(input('LARGURA: (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
