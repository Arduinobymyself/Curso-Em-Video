"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

v = float(input('Qual é a velocidade atual: '))
if v > 80:
    print('Você está {}Km/h acima da velocidade pemitida \ne pagará R${:.2f} de multa!'.format((v-80), (v-80)*7))
    print("RESPEITE AS LEIS DE TRANSITO!")
else:
    print('Parabéns! \nvocê está respeitando o limite de velocidade de 80Km/h.')