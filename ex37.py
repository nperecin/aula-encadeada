valor = float(input("Digite o valor da compra: R$ "))

if valor >= 200:
    vip = input("O cliente é VIP? (sim/não): ").strip().lower()

    if vip == "sim":
        print("Desconto VIP")
    else:
        print("Desconto comum")
else:
    print("Sem desconto")