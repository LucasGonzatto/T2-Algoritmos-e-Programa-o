def ler_csv(nome):
    try:
        with open(nome, 'r') as arq:
            linhas = arq.readlines()
        return [linha.strip().split(',') for linha in linhas[1:]]
    except:
        print("Erro ao abrir arquivo")
        return []
nome = input("Nome do arquivo CSV: ")
print(ler_csv(nome))
