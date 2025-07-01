while True:
    nome = input("Nome do atleta (enter para sair): ")
    if nome == "":
        break
    saltos = []
    for i in range(5):
        salto = float(input(f"{i+1}º salto: "))
        saltos.append(salto)
    melhor = max(saltos)
    pior = min(saltos)
    media = (sum(saltos) - melhor - pior) / 3
    print("Melhor salto:", melhor)
    print("Pior salto:", pior)
    print("Média dos demais saltos:", round(media, 2))
    print(f"Resultado final: {nome}: {round(media, 2)} m")
