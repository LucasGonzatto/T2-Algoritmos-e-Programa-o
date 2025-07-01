divida = float(input("Digite o valor da dívida: "))
print("Valor da Dívida | Juros | Parcelas | Valor da Parcela")
parcelas_juros = [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]
for p, j in parcelas_juros:
    val_juros = divida * (j / 100)
    total = divida + val_juros
    parc = total / p
    print(f"R$ {total:.2f}      | {j}%   | {p}       | R$ {parc:.2f}")
