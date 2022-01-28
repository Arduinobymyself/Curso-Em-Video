"""
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e
condição de pagamento:
à vista dinheiro / cheque: 10% de desconto
à vista no cartão: 5% de desconto
em até 2x no cartão: preço normal
3x ou mais no cartão: 20% de juros
"""
print("{:=^40}".format(" LOJAS MORAES "))
valor = float(input("Digite o valor do produto R$"))
print("""\nEscolha a forma de pagamento
[1] à vista em dinheiro com 10% de desconto
[2] à vista no cartão com 5% de desconto
[3] em 2x no cartão com preço normal
[4] em 3x ou mais no cartão com 20% de acréscimo\n""")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    desconto = valor - valor*10/100
    print("O valor a ser pago é de R${:.2f}".format(desconto))
elif opcao == 2:
    desconto = valor - valor*5/100
    print("O valor a ser pago é de R${:.2f}".format(desconto))
elif opcao == 3:
    parcelas = 2
    print("Sua compra será parcelada em {}x de R${:.2f} \033[32mSEM JUROS\033[m".format(parcelas, valor / parcelas))
elif opcao == 4:
    parcelas = int(input("Em quantas parcelas? "))
    acrescimo = valor + valor*20/100
    print("Sua compra será parcelada em {}x de R${:.2f} \033[31mCOM JUROS de 20%\033[m".format(parcelas, acrescimo/parcelas))
    print("O valor total a ser pago é de \033[31mR${:.2f}\033[m".format(acrescimo))
else:
    print("\n\033[31mOpção inválida, tente novamente\033[m")
