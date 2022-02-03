dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
print(dados[1])

pessoas = list()
pessoas.append(dados[:])
print(pessoas[0])

pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[1])
print(pessoas[1][0])
print(pessoas[1][1])