"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado.
"""
#aquisição das informações
valor = float(input("Valor da casa R$"))
salario = float(input("Salário do comprador R$"))
anos = int(input("Quantos anos de financiamento? "))

#cálculos
prestacao = valor/(anos*12)
minimo = salario*30/100

print("Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}".format(valor, anos, prestacao))

#verificação e validação
if prestacao>minimo:
    print("Empréstimo NEGADO!")
else:
    print("Empréstimo pode ser CONCEDIDO!")
