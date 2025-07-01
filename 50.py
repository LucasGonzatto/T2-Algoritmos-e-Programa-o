n = int(input("Digite o valor de N: "))
h = 0
for i in range(1, n + 1):
    h += 1 / i
print("Valor de H:", round(h, 2))
