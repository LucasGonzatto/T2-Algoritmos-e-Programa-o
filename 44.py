votos = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total = 0
while True:
    voto = int(input("Digite seu voto (1-4 candidatos, 5 nulo, 6 branco, 0 sair): "))
    if voto == 0:
        break
    if voto in votos:
        votos[voto] += 1
        total += 1
    else:
        print("Voto inválido.")
print("Resultado:")
for i in range(1, 5):
    print(f"Candidato {i}: {votos[i]} votos")
print("Nulos:", votos[5])
print("Brancos:", votos[6])
print("Percentual nulos:", (votos[5] / total) * 100 if total else 0, "%")
print("Percentual brancos:", (votos[6] / total) * 100 if total else 0, "%")
