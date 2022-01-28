"""
Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher
qual será a base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal
"""
n = int(input("Digite um número inteiro: "))
b = int(input("Qual será a base de conversão?\n"
      "1 - BINÁRIO\n"
      "2 - HEXADECIMAL\n"
      "3 - OCTAL\n"
      "Opção: "))

if b<1 or b>3:
      print("Opção inválida, tente novamente")
else:
      if b == 1:
            print("{} convertido para Binário = {}".format(n, bin(n)[2:]))
      elif b == 2:
            print("{} convertido para Hexadecimal = {}".format(n, hex(n)[2:]))
      elif b == 3:
            print("{} convertido para Octal = {}".format(n,oct(n)[2:]))
