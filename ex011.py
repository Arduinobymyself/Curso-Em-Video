l = float(input('Entre com a largura: '))
a = float(input("Entre com a altura: "))
area = a * l
tinta = area / 2

print('A parede de {}x{} tem área de {:.1f}m^2, \nserão necessários {:.1f}l de tinta para pintá-la.'.format(l, a, area, tinta))
