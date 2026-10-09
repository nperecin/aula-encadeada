idade = int(input("Digite sua idade: "))

if idade >= 18:
    ingresso = input("Você possui ingresso? (sim/não): ").lower()

    if ingresso == "sim":
        print("Entrada permitida")
    else:
        print("Ingresso necessário")
else:
    print("Idade insuficiente")