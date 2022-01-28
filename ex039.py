"""
Escreva um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade:
- se ele ainda vai se alistar ao serviço militar.
- se é a hora de se alistar.
- se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

nasc = int(input("Em que ano você nasceu: "))
atual = date.today().year
idade = atual - nasc

print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))



if idade == 18:
    print("Você deve se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo = 18 - idade
    print("Ainda faltam {} anos para o alistamento militar.".format(saldo))
    print("Você deverá se alistar em {}".format(atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print("Você já deveria ter se alistado há {} anos.".format(saldo))
    print("Seu alistamento foi em {}".format(atual - saldo))
