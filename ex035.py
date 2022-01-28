"""
Desenvolva um programa que leia o comprimento de
três retas e diga ao usuário se elas podem ou não
formar um triângulo.
"""
print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)

r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))

if (r1+r2)>r3 and (r1+r3)>r2 and (r2+r3)>r1:
    print('Os segmentos de retas acima PODEM formar um Triângulo')
else:
    print('Os segmentos de retas acima NÃO PODEM formar um Triângulo')
