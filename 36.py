n = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))
if inicio > fim:
    print("Intervalo inválido.")
else:
    print(f"Vou montar a tabuada de {n} começando em {inicio} e terminando em {fim}:")
    for i in range(inicio, fim + 1):
        print(f"{n} x {i} = {n * i}")
