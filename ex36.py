media = float(input("Digite a média do aluno: "))
frequencia = float(input("Digite a frequência percentual: "))

if media >= 7:
    if frequencia >= 75:
        print("Aprovado")
    else:
        print("Reprovado por frequência")
else:
    print("Reprovado por média")