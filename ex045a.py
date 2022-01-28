from random import randint

usuario = 0
computador = 0
usuario_venceu = 0
computador_venceu = 0

jogadas = ["pedra", "papel", "tesoura"]

while True:
    usuario = input("Digite Pedra/Papel/Tesoura ou S para sair: ").lower()
    if usuario == "s":
        break

    if usuario not in jogadas:
        continue

    numero = randint(0, 2)
    # pedra: 0, papel: 1, tesoura: 2
    computador = jogadas[numero]
    print("Computer jogou {}.".format(computador))
    if usuario == computador:
        print("Empatamos!")
    elif (usuario == "pedra" and computador == "tesoura") \
        or (usuario == "papel" and computador == "pedra") \
        or (usuario == "tesoura" and computador == "papel"):
        print("Você venceu!")
        usuario_venceu += 1
    else:
        print("Voce perdeu!")
        computador_venceu += 1

print("Você venceu {} vezes.".format(usuario_venceu))
print("Computador venceu {} vezes.".format(computador_venceu))
print("Até Logo!")