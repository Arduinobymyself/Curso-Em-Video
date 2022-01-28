"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

print('-' * 20)
print(' LOJA SUPER BARATÃO')
print('-' * 20)

total = cont = maior1000 = precoMaisBarato = 0
nomeMaisBarato = ' '

while True:
    nome = input('Nome do produto: ').strip()
    preco = float(input('Valor do produto R$ '))

    cont += 1
    total += preco

    if preco > 1000:
        maior1000 += 1

    if cont == 1 or preco < precoMaisBarato:
        precoMaisBarato = preco
        nomeMaisBarato = nome

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior1000} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMaisBarato} que custa R${precoMaisBarato:.2f}')
