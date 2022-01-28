"""
A confederação nacional de natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
até 9 anos - MIRIM
até 14 anos - INFANTIL
até 19 anos - JUNIOR
até 20 anos - SÊNIOR
acima - MASTER
"""

from datetime import date

atual = date.today().year

nasc = int(input("Qual o ano de nascimento: "))
idade = atual - nasc

print("O atleta tem {} anos".format(idade))


if idade <= 9:
    print("Categoria MIRIM.")
elif idade <= 14:
    print("Categoria INFANTIL.")
elif idade <= 19:
    print("Categoria JUNIOR.")
elif idade <= 25:
    print("Categoria SENIOR.")
elif idade > 25:
    print("Categoria MASTER.")