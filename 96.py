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
def somar_em_bases(lista, base_origem, base_destino):
    total = 0
    for num in lista:
        val = base_para_decimal(num, base_origem)
        if val is not None:
            total += val
    return decimal_para_base(total, base_destino)
