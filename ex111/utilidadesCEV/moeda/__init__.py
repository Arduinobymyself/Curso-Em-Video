

def aumentar(preco=0, taxa=0, formatado=False):
    res = preco + preco*taxa/100
    return res if formatado is False else moeda(res)


def diminuir(preco=0, taxa=0, formatado=False):
    res = preco - preco*taxa/100
    return res if formatado is False else moeda(res)


def dobro(preco=0, formatado=False):
    res = preco*2
    return res if formatado is False else moeda(res)


def metade(preco=0, formatado=False):
    res = preco/2
    return res if formatado is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    res = f'{moeda}{preco:>.2f}'.replace('.', ',')
    return res


def resumo(preco=0, taxaa=10, taxar=5):
    mensagem('-', 'RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: {aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: {diminuir(preco, taxar, True)}')
    mensagem('-', 'FIM')




def mensagem(moldura, texto):
    comp = len(texto)
    print(moldura*(comp + 10))
    print('|    ' + f'{texto}' + '    |')
    print(moldura*(comp+10))
    print()
