n = int(input("Digite um número: "))
divs = []
for i in range(1, n + 1):
    if n % i == 0:
        divs.append(i)
if len(divs) == 2:
    print(f"{n} é primo.")
else:
    print(f"{n} não é primo. Divisores: {divs}")
