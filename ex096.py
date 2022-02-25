'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.
'''

def area(largura, comprimento):
  return largura * comprimento


print(' Controle de Terenos ')
print('-'*21)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
print(f"A área de um terreno {larg} x {comp} é de {area(larg, comp)}m²")
