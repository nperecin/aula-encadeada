saldo = float(input("Digite o saldo disponível: R$ "))
compra = float(input("Digite o valor da compra: R$ "))

if saldo >= compra:
    confirmar = input("Deseja confirmar a compra? (sim/não): ").lower()

    if confirmar == "sim":
        print("Compra realizada")
    else:
        print("Compra cancelada")
else:
    print("Saldo insuficiente")