nome = str(input('Qual é o seu nome? ')).strip()
if nome.upper() == 'MARCELO':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))