def somaarquivo(nome):
    try:
        with open(nome, 'r') as arq:
            total = 0
            for linha in arq:
                try:
                    total += int(linha.strip())
                except:
                    continue
        return total
    except:
        print("Erro ao abrir arquivo")
        return 0
nome = input("Arquivo com números: ")
print("Soma:", somaarquivo(nome))
