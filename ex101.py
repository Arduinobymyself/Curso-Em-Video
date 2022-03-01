'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e
OBRIGATÓRIO nas eleições.
'''

def voto(ano):
    """
    função para verificar situação de voto
    :param ano: ano de nascimento
    :return: idade e situação de voto
    """
    from datetime import date

    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade > 65 or 16 <= idade < 18:
        return f'Com {idade}, o voto é OPCIONAL'
    elif idade < 16:
        return f'Com {idade}, o voto é NEGADO'
    else:
        return f'Com {idade}, o voto é OBRIGATÓRIO'


print('-='*30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))
