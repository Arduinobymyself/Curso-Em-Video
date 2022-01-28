"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
"""

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
         'Bragantino', 'Fliminense', 'América-MG', 'Atlético-GO', 'Santos',
         'Ceará-SC', 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá',
         'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print('-='*30)
print(f'Lista de times do Basileirão 2021: {times}')
print('-='*30)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*30)
print(f'Os quatro últimos são {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*30)
for p, c in enumerate(times):
    if times[p] == 'Chapecoense':
        print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*30)