"""
desafio 23
Faça um programa que leia um número de 0 a 999 e mostre na tela cada um dos digitos separados.
Ex:
Digite um número: 1834
unidade: 4
dezenas: 3
centena: 8
milhar: 1
"""
#entrada de dados
n = int(input('Digite um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade : {}'.format(u))
print('Dezena  : {}'.format(d))
print('Centena : {}'.format(c))
print('Milhar  : {}'.format(m))

""" Old Solution (string)
n = str(input('Digite um número entre 0 e 9999: '))
aux = n 
print('Milhar  : {}'.format(n[:1]))
print('Centena : {}'.format(n[1:2]))
print('Dezena  : {}'.format(n[2:3]))
print('Unidade : {}'.format(n[3:]))
"""