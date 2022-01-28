dias = int(input('Quantos dia alugado? '))
km = float(input('Quantos Km rodados? '))
total = 60 * dias + 0.15 * km
print('O total a pagar é de R${:.2f}'.format(total))