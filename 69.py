def contar_palavras(frases):
    contagem = {}
    for frase in frases:
        palavras = frase.lower().split()
        for palavra in palavras:
            palavra = ''.join(c for c in palavra if c.isalnum())
            if palavra:
                contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem
lista = ["Olá mundo", "Olá Python", "Python é bom"]
print(contar_palavras(lista))
