from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
h = hypot(ca, co)
print('A hipotenusa mede: {:.2f}'.format(h))
