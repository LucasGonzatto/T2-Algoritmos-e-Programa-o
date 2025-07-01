faixa1 = faixa2 = faixa3 = faixa4 = 0
while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    if 0 <= num <= 25:
        faixa1 += 1
    elif 26 <= num <= 50:
        faixa2 += 1
    elif 51 <= num <= 75:
        faixa3 += 1
    elif 76 <= num <= 100:
        faixa4 += 1
print("[0-25]:", faixa1)
print("[26-50]:", faixa2)
print("[51-75]:", faixa3)
print("[76-100]:", faixa4)
