menor = None
maior = None
soma = 0
cont = 0
while True:
    try:
        temp = float(input("Digite a temperatura (ou ENTER para sair): "))
        soma += temp
        cont += 1
        if menor is None or temp < menor:
            menor = temp
        if maior is None or temp > maior:
            maior = temp
    except:
        break
if cont > 0:
    print("Menor temperatura:", menor)
    print("Maior temperatura:", maior)
    print("Média das temperaturas:", soma / cont)
