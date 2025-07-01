n = int(input("Digite um número para ver a tabuada (1 a 10): "))
print(f"Tabuada de {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
