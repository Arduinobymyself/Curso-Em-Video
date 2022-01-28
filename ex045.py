"""
Crie um progrma que faça o computador
jogar jokenpô com você
"""

from random import choice
from time import sleep


print("{:=^40}".format(" Vamos Jogar!? "))
print("{:=^40}".format(" jokenpô!!! n"))

lista = ["Pedra", "Tesoura", "Papel"]
computer = choice(lista)

print("""Já escolhi!...\n
[1] Pedra
[2] Tesoura
[3] Papel""")

human = int(input("... faça sua escolha: "))
if 1 <= human <= 3:
    human = lista[human-1]
    print("Jooo... ")
    sleep(1)
    print("keeen... ")
    sleep(1)
    print("Pôoo!!!\n")

    print("Minha escolha foi {}, a sua foi {}.".format(computer, human))

    if human == "Pedra":
        if computer == "Pedra":
            print("Empatamos!!!")
        elif computer == "Papel":
            print("Eu ganhei! - Papel embrulha Pedra")
        elif computer == "Tesoura":
            print("Você ganhou! - Pedra quebra Tesoura")

    elif human == "Papel":
        if computer == "Papel":
            print("Empatamos!!!")
        elif computer == "Tesoura":
            print("Eu ganhei! - Tesoura corta Papel")
        elif computer == "Pedra":
            print("Você ganhou! - Papel embrulha Pedra")

    elif human == "Tesoura":
        if computer == "Tesoura":
            print("Empatamos!!!")
        elif computer == "Pedra":
            print("Eu ganhei! - Pedra quebra Tesoura")
        elif computer == "Papel":
            print("Você ganhou! - Tesoura corta Papel")
else:
    print("\033[31mEscolha inválida!, tente novamente.\033[m")

