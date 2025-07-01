n = int(input("Digite um número: "))
div = 0
for i in range(1, n + 1):
    if n % i == 0:
        div += 1
if div == 2:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo.")
