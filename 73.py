def filtranumeros(lista, tipo):
    if tipo == 'pares':
        return [n for n in lista if n % 2 == 0]
    elif tipo == 'impares':
        return [n for n in lista if n % 2 != 0]
    elif tipo == 'positivos':
        return [n for n in lista if n > 0]
    elif tipo == 'negativos':
        return [n for n in lista if n < 0]
    return []
nums = [int(n) for n in input("Digite os números separados por espaço: ").split()]
tipo = input("Tipo (pares, impares, positivos, negativos): ")
print(filtranumeros(nums, tipo))
