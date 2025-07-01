linhas = int(input("Linhas: "))
colunas = int(input("Colunas: "))
maior = menor = None
for i in range(linhas):
    for j in range(colunas):
        num = int(input(f"Elemento [{i}][{j}]: "))
        if maior is None or num > maior:
            maior = num
        if menor is None or num < menor:
            menor = num
print("Maior elemento:", maior)
print("Menor elemento:", menor)
