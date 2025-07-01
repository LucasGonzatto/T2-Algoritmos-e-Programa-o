linhas = int(input("Número de linhas: "))
colunas = int(input("Número de colunas: "))
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"Elemento [{i}][{j}]: ")))
    matriz.append(linha)
x = int(input("Elemento a contar: "))
cont = sum(linha.count(x) for linha in matriz)
print(f"O elemento {x} aparece {cont} vezes.")
