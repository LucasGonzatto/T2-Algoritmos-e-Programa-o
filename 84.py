def substituir_arquivo(nome, antigo, novo):
    try:
        with open(nome, 'r') as arq:
            conteudo = arq.read()
        conteudo = conteudo.replace(antigo, novo)
        with open(nome, 'w') as arq:
            arq.write(conteudo)
    except:
        print("Erro ao abrir/modificar o arquivo")
nome = input("Arquivo: ")
antigo = input("Texto antigo: ")
novo = input("Texto novo: ")
substituir_arquivo(nome, antigo, novo)
