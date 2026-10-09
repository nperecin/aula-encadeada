matriculado = input("Você está matriculado? (sim/não): ").strip().lower()

if matriculado == "sim":
    autorizacao = input("Você possui autorização? (sim/não): ").strip().lower()

    if autorizacao == "sim":
        print("Acesso permitido")
    else:
        print("Autorização necessária")
else:
    print("Matrícula necessária")