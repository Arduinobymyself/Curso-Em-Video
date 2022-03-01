'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() 
que receba dois parâmetros: o primeiro que indique o número a calcular e 
outro chamado show, que será um valor lógico (opcional) indicando se será 
mostrado ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(num=1, show=False):
    """
    Função para calculo do fatorial de um número inteiro
    :param num: inteiro, o número a ser calculado
    :param show: boolean, parâmetro opcional (mostar ou não a conta efetuada)
    :return: inteiro, o valor do fatorial de num calculao
    """

    f = 1

    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('= ', end='')
    return f


print(fatorial(7, True))
print()
help(fatorial) # chamada do help interativo da função

