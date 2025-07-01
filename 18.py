qtd = int(input("Quantos números deseja digitar? "))
menor = None
maior = None
soma = 0
for i in range(qtd):
    num = float(input(f"Digite o {i+1}º número: "))
    soma += num
    if menor is None or num < menor:
        menor = num
    if maior is None or num > maior:
        maior = num
print("Menor:", menor)
print("Maior:", maior)
print("Soma:", soma)
