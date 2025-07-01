def copiararquivo(origem, destino):
    try:
        with open(origem, 'r') as arq1:
            conteudo = arq1.read()
        with open(destino, 'w') as arq2:
            arq2.write(conteudo)
    except:
        print("Erro ao copiar arquivo")
origem = input("Arquivo origem: ")
destino = input("Arquivo destino: ")
copiararquivo(origem, destino)
