"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de
mostrar que tipo de triângulo será formado:
EQUILÁTERO - todos os lados iguais
ISÓCELES - dois lados iguais
ESCALENO todos os lados diferentes
"""

print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))

if not(r1+r2)>r3 or not(r1+r3)>r2 or not(r2+r3)>r1:
    print('Os segmentos de retas NÃO PODEM formar um Triângulo')
elif r1 == r2 == r3:
    print("Os segmentos de reta formam um Triângulo EQUILÁTERO")
elif r1 != r2 != r3 != r1:
    print("Os segmentos de reta formam um Triângulo ESCALENO")
elif r1==r2 or r2==r3 or r3==r1:
    print("Os segmentos de reta formam um Triângulo ISÓCELES")


