n = int(input("Tamanho da matriz quadrada: "))
matriz = []
for i in range(n):
    linha = []
    for j in range(n):
        num = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(num)
    matriz.append(linha)
soma_principal = sum(matriz[i][i] for i in range(n))
soma_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))
print("Soma diagonal principal:", soma_principal)
print("Soma diagonal secundária:", soma_secundaria)
