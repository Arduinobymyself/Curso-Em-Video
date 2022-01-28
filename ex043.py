"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa,
calcule o seu IMC e mostre seu status, de acordo
com a tabela abaixo:
abaixo de 18.5 - ABAIXO DO PESO
de 18.5 e 25 - PESO IDEAL
de 25 a 30 - SOBREPESO
de 30 até 40 - OBESIDADE
acima de 40 - OBESIDADE MÓRBIDA
"""

peso = float(input("Digite seu peso em Kilogramas: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso/(altura*altura)

print("Seu ìndice de Massa Corporal (IMC) é de {:.1f}: ".format(imc))

if imc < 17:
    print("Muito  abaixo do peso")
elif imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Acima do peso")
elif imc < 35:
    print("Obesidade I")
elif imc < 40:
    print("Obesidade II (Severa)")
else:
    print("Obesidade III (Mórbida")
