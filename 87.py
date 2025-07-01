def numerar_linhas(origem, destino):
    try:
        with open(origem, 'r') as arq:
            linhas = arq.readlines()
        with open(destino, 'w') as novo:
            for i, linha in enumerate(linhas):
                novo.write(f"{i+1} {linha}")
    except:
        print("Erro ao processar arquivo")
origem = input("Arquivo origem: ")
destino = input("Arquivo destino: ")
numerar_linhas(origem, destino)
