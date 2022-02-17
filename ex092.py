'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e
carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.
'''

from datetime import datetime

cadastro = dict()

cadastro['nome'] = str(input("Nome: "))
nascimento = int(input('Ano de Nascimento: '))
idade = datetime.now().year - nascimento
cadastro['idade'] = idade
ctps = int(input('Carterira de Trabalho (0 não tem): '))
if ctps != 0:
    cadastro['ctps'] = ctps
    cadastro['contratação'] = int(input("Ano de Contratação: "))
    cadastro['aposentadoria'] = cadastro['contratação'] + 35
    cadastro['salario'] = float(input("Salário R$ "))


print('-='*30)
#  print(cadastro)
for k, v in cadastro.items():
    print(f'{k} = {v}')
