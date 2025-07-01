def ler_arquivo(nome):
    try:
        with open(nome, 'r') as arq:
            print(arq.read())
    except:
        print("Erro ao abrir arquivo")
nome = input("Nome do arquivo: ")
ler_arquivo(nome)
