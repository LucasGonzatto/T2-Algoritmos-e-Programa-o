votos1 = 0
votos2 = 0
votos3 = 0
eleitores = int(input("Número de eleitores: "))
for i in range(eleitores):
    voto = int(input(f"Eleitor {i+1}, vote (1, 2 ou 3): "))
    if voto == 1:
        votos1 += 1
    elif voto == 2:
        votos2 += 1
    elif voto == 3:
        votos3 += 1
    else:
        print("Voto inválido")
print("Candidato 1:", votos1, "votos")
print("Candidato 2:", votos2, "votos")
print("Candidato 3:", votos3, "votos")
