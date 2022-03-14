
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO!\"{entrada}\" é um preço inválido!\033[m')
        else:
            return float(entrada)

def leiaInt(msg):
    flag = False
    n = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            flag = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            print()
        if flag:
            break
    return int(n)