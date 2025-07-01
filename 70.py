import random
import string
def gerar_senha(tam, usar_numeros=True, usar_simbolos=False):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = '!@#$%^&*'
    caracteres = letras
    if usar_numeros:
        caracteres += numeros
    if usar_simbolos:
        caracteres += simbolos
    return ''.join(random.choice(caracteres) for _ in range(tam))
tam = int(input("Comprimento da senha: "))
num = input("Incluir números? (s/n): ").lower() == 's'
sim = input("Incluir símbolos? (s/n): ").lower() == 's'
print("Senha gerada:", gerar_senha(tam, num, sim))
