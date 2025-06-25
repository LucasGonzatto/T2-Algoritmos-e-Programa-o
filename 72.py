def converter_temp(valor, origem, destino):
    if origem == destino:
        return valor
    if origem == 'C':
        if destino == 'F':
            return valor * 1.8 + 32
        elif destino == 'K':
            return valor + 273.15
    elif origem == 'F':
        if destino == 'C':
            return (valor - 32) / 1.8
        elif destino == 'K':
            return (valor - 32) / 1.8 + 273.15
    elif origem == 'K':
        if destino == 'C':
            return valor - 273.15
        elif destino == 'F':
            return (valor - 273.15) * 1.8 + 32
    return "Erro nas unidades"
v = float(input("Valor: "))
orig = input("Origem (C, F ou K): ").upper()
dest = input("Destino (C, F ou K): ").upper()
print("Resultado:", converter_temp(v, orig, dest))
