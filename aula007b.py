n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
r = n1 % n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} \n a divisão é {:.3f} e o resto é {}'.format(s, m, d, r), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))