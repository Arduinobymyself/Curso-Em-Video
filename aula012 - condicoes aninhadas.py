nome = str(input("Qual é o seu nome? "))
if nome == 'Marcelo':
    print("que belo nome!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print("Seu nome é bem popular no Brasil.")
elif nome in 'Ana Claudia Jéssica Juliana':
    print("Belo nome feminino.")
else:
    print("Seu nome é bem comum.")
print("Tenha um bom dia, {}".format(nome))

