DIGITOS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def decimal_para_base(n, base):
    if not (2 <= base <= len(DIGITOS)): return "Base inválida"
    if n == 0: return "0"
    res = ""
    while n:
        n, r = divmod(n, base)
        res = DIGITOS[r] + res
    return res
class DigitoDisplay:
    mapa = {
        '0': ["***", "* *", "* *", "* *", "***"],
        '1': [" * ", "** ", " * ", " * ", "***"],
        '2': ["***", "  *", "***", "*  ", "***"],
        '3': ["***", "  *", "***", "  *", "***"],
        '4': ["* *", "* *", "***", "  *", "  *"],
        '5': ["***", "*  ", "***", "  *", "***"],
        '6': ["***", "*  ", "***", "* *", "***"],
        '7': ["***", "  *", " * ", " * ", " * "],
        '8': ["***", "* *", "***", "* *", "***"],
        '9': ["***", "* *", "***", "  *", "***"],
        'A': ["***", "* *", "***", "* *", "* *"],
        'B': ["** ", "* *", "** ", "* *", "** "],
        'C': ["***", "*  ", "*  ", "*  ", "***"],
        'D': ["** ", "* *", "* *", "* *", "** "],
        'E': ["***", "*  ", "***", "*  ", "***"],
        'F': ["***", "*  ", "***", "*  ", "*  "],
    }
    def __init__(self, dig):
        self.representacao = DigitoDisplay.mapa.get(dig.upper(), ["   "] * 5)
    def obter(self):
        return self.representacao
class DisplayDigital:
    def __init__(self, num_digitos):
        self.num_digitos = num_digitos
        self.digitos = ['0'] * num_digitos
    def exibir_numero(self, numero, base):
        try:
            convertido = decimal_para_base(int(numero), base).upper()
        except ValueError:
            print("Erro: Entrada inválida.")
            return
        if len(convertido) > self.num_digitos:
            print("Erro: Número muito grande para o display")
            return
        self.digitos = list(convertido.rjust(self.num_digitos))
    def renderizar(self):
        linhas = ['' for _ in range(5)]
        for dig in self.digitos:
            rep = DigitoDisplay(dig).obter()
            for i in range(5):
                linhas[i] += rep[i] + '  '
        print("\n".join(linhas))
