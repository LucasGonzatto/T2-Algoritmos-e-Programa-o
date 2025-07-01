def escreverarq(nome, conteudo):
    with open(nome, 'w') as arq:
        arq.write(conteudo)
nome = input("Nome do arquivo: ")
texto = input("Conteúdo: ")
escreverarq(nome, texto)
