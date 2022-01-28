"""
Escreva um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
média abaixo de 5.0 : REPROVADO
média entre 5.0 e 6.9 : RECUPERAÇÃO
média 7.0 ou superior : APROVADO
"""

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1+n2)/2

if media < 5:
    print("A sua média é {:.1f}, você foi REPROVADO!".format(media))
elif media >=5 and media < 7:
    print("A sua média é {:.1f}, você ficou de RECUPERAÇÃO!".format(media))
elif media >= 7:
    print("A sua média é {:.1f}, você foi APROVADO!".format(media))