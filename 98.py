def decimal_para_base(numero, base):
    if numero == 0:
        return "0"
    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while numero > 0:
        res = digitos[numero % base] + res
        numero //= base
    return res
def encontrar_palindromos_base(lista_decimais, base):
    resultado = []
    for num in lista_decimais:
        convertido = decimal_para_base(num, base)
        if convertido == convertido[::-1]:
            resultado.append(num)
    return resultado
