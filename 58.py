linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)
matrizinvertida = matriz[::-1]
for linha in matrizinvertida:
    print(linha)
