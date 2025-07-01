DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def base_para_decimal(s: str, base: int) -> int | None:
    try:
        return sum(DIGITOS.index(c) * base**i for i, c in enumerate(reversed(s.upper())))
    except ValueError:
        return None
def decimal_para_base(n: int, base: int) -> str:
    if not (2 <= base <= len(DIGITOS)): return "Base inválida"
    if n == 0: return "0"
    s = ""
    while n:
        n, r = divmod(n, base)
        s = DIGITOS[r] + s
    return s
def operacao(num1: str, num2: str, base_in: int, op: str, base_out: int) -> str:
    a, b = base_para_decimal(num1, base_in), base_para_decimal(num2, base_in)
    if a is None or b is None: return "Erro na conversão"
    match op:
        case '+': res = a + b
        case '-': res = a - b
        case '*': res = a * b
        case '/':
            if b == 0: return "Erro: divisão por zero"
            res = a // b
        case _: return "Operação inválida"
    return decimal_para_base(res, base_out)
