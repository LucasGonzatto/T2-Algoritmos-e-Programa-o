def anexararquivo(nome, conteudo):
    with open(nome, 'a') as arq:
        arq.write(conteudo)
nome = input("Nome do arquivo: ")
texto = input("Texto a adicionar: ")
anexararquivo(nome, texto)
