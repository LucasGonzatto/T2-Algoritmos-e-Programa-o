matriz = []
while True:
    linha = input("Digite uma linha de números separados por espaço (ou vazio para sair): ")
    if linha == "":
        break
    matriz.append([int(x) for x in linha.split()])
quadrada = all(len(linha) == len(matriz) for linha in matriz)
print("É quadrada e válida?", quadrada)
