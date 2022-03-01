'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help
do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.
'''

from time import sleep


# cores para o sistema
cores = ('\033[m',         # 0 - sem cores
         '\033[0;30;41m',  # 1 - vermelho
         '\033[0;30;42m',  # 2 - verde
         '\033[0;30;43m',  # 3 - amarelo
         '\033[0;30;44m',  # 4 - azul
         '\033[0;30;45m',  # 5 - roxo
         '\033[7;30m'      # 6 - branco
        )


# função que retorna o help interativo do comando solicitado
def ajuda(comando):
  mensagem('-', f'Acessando o manual do comando {comando}', 2)
  print(cores[3], end='')
  help(comando)
  print(cores[0], end='')
  sleep(2)


# função que gera moldura e mensagem
def mensagem(moldura, texto, cor=0):
  comp = len(texto)
  print(cores[cor], end='')
  print(moldura*(comp + 10))
  print('|    ' + f'{texto}' + '    |')
  print(moldura*(comp+10))
  print(cores[0], end='')
  sleep(1)


# programa principal
comando = ' '
while True:
  mensagem('~', 'SISTEMA DE AJUDA PyHELP', 4)
  comando = str(input('Função ou Biblioteca > '))
  if comando.upper() == 'FIM':
    break
  else:
    ajuda(comando)
mensagem('~', 'ATÉ LOGO!', 1)


