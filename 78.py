def contarlinhas(nome):
    try:
        with open(nome, 'r') as arq:
            return len(arq.readlines())
    except:
        print("Erro ao abrir arquivo")
        return 0
nome = input("Nome do arquivo: ")
print("Total de linhas:", contarlinhas(nome))
