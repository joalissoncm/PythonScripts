#Programa recebe o cateto oposto e o adjacente e retorma o comprimento da hipotenusa

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipot = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hipot))
