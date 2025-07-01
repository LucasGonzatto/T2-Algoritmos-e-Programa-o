def base_para_decimal(numero, base):
    mapa = '0123456789ABCDEF'
    numero = numero.upper()
    valor = 0
    for i, digito in enumerate(reversed(numero)):
        if digito not in mapa[:base]:
            return None
        valor += mapa.index(digito) * (base ** i)
    return valor
def decimal_para_base(valor, base):
    mapa = '0123456789ABCDEF'
    if valor == 0:
        return '0'
    resultado = ''
    while valor > 0:
        resultado = mapa[valor % base] + resultado
        valor //= base
    return resultado
def converter_base(numero_str, base_origem, base_destino):
    decimal = base_para_decimal(numero_str, base_origem)
    if decimal is None:
        return "Número inválido para a base"
    return decimal_para_base(decimal, base_destino)
num = input("Número: ")
origem = int(input("Base de origem: "))
destino = int(input("Base de destino: "))
print("Convertido:", converter_base(num, origem, destino))
