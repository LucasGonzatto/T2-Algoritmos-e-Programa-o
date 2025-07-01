def combinarlistas(*listas):
    resultado = []
    for l in listas:
        resultado += l
    return resultado
a = [1, 2, 3]
b = [4, 5]
c = [6]
print(combinarlistas(a, b, c))
