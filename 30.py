preco = float(input("Preço do pão: R$ "))
print("Panificadora Pão de Ontem - Tabela de preços")
for i in range(1, 51):
    valor = i * preco
    print(f"{i} - R$ {valor:.2f}")
