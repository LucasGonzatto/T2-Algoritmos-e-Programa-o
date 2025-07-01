texto = input("Digite o texto: ")
padrao = input("Digite o padrão: ")
print("É prefixo?", texto.startswith(padrao))
print("É sufixo?", texto.endswith(padrao))
