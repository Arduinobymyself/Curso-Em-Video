"""
Escreva um progama que leia dois números inteiros e
compare-os, mostrando na tela uma mensagem:
o primeiro valor é maior
o segundo valor é maior
não existe valor maior, os dois são iguais
"""
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1>n2:
    print("{} é maior do que {}".format(n1, n2))
elif n2>n1:
    print("{} é maior do que {}".format(n2, n1))
else:
    print("Os dois números são iguais, não existe maior!")
