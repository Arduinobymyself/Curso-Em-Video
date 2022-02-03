teste = list()
teste.append('Marcelo')
teste.append(50)
galera = list()
galera.append(teste[:])
print(galera)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('-=' * 30)

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-=' * 30)

galera = list()
dado = list()
for c in range(0, 4):
    dado.append(str(input('Nome:  ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('-=' * 30)
totMaior = totMenor = 0
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totMaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totMenor += 1
print(f'Temos {totMaior} maiores e {totMenor} menores de idade.')
print('-=' * 30)
