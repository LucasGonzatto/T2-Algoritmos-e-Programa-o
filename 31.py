while True:
    total = 0
    cont = 1
    print("Lojas Tabajara")
    while True:
        valor = float(input(f"Produto {cont}: R$ "))
        if valor == 0:
            break
        total += valor
        cont += 1
    print("Total: R$", total)
    dinheiro = float(input("Dinheiro: R$ "))
    troco = dinheiro - total
    print("Troco: R$", troco)
    novo = input("Registrar nova compra? (s/n): ").lower()
    if novo != 's':
        break
