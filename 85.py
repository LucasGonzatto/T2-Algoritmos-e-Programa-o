def filtrar_linhas(origem, destino, chave):
    try:
        with open(origem, 'r') as arq:
            linhas = arq.readlines()
        with open(destino, 'w') as novo:
            for linha in linhas:
                if chave.lower() in linha.lower():
                    novo.write(linha)
    except:
        print("Erro ao acessar os arquivos")
origem = input("Arquivo origem: ")
destino = input("Arquivo destino: ")
chave = input("Palavra-chave: ")
filtrar_linhas(origem, destino, chave)