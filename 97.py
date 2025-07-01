def validar_numeros_base(lista, base):
    validos = []
    mapa = '0123456789ABCDEF'[:base]
    for num in lista:
        num = num.upper()
        if all(c in mapa for c in num):
            validos.append(num)
    return validos
lista = ['10', '1G', '1010', 'A']
base = 16
print("Números válidos:", validar_numeros_base(lista, base))
