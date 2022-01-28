"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a
maioridade e quantas já são maiores.
"""
from datetime import date


ano_atual = date.today().year

contador = 0

for c in range(1, 8):
    ano = int(input('digite o ano de nascimento da {}ª pessoa: '.format(c)))
    if (ano_atual - ano) < 21:
        contador += 1
print('{} de {} não são maiores de idade, ou seja {:.2f}%.'.format(contador, 7, contador/7*100))
