while True:
    nome = input("Nome do ginasta (enter para sair): ")
    if nome == "":
        break
    notas = []
    for i in range(7):
        nota = float(input(f"Nota {i+1}: "))
        notas.append(nota)
    melhor = max(notas)
    pior = min(notas)
    notas.remove(melhor)
    notas.remove(pior)
    media = sum(notas) / len(notas)
    print("Resultado final:")
    print("Atleta:", nome)
    print("Melhor nota:", melhor)
    print("Pior nota:", pior)
    print("Média:", round(media, 2))
