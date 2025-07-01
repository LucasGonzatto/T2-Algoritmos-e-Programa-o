qtd = int(input("Quantos CDs você tem? "))
total = 0
for i in range(qtd):
    preco = float(input(f"Valor do CD {i+1}: R$ "))
    total += preco
media = total / qtd
print("Total investido: R$", total)
print("Valor médio por CD: R$", media)
