"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por K para
viagens de até 200Km e R$0,45 para viagens mais longas
"""
dist = float(input('Qual a distância da sua viagem?: '))
print('Você está prestes a começar uma viagem de {}'.format(dist))
passagem = dist*0.45 if dist>=200 else dist*0.50
print('E o preço da sua passagem será de R${:.2f}'.format(passagem))


"""
if dist > 200:
    passagem = dist*0.45
else:
    passagem = dist*0.50
print('E o preço da sua passagem será de R${:.2f}'.format(passagem))
"""
