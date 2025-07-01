n = int(input("Digite um número para calcular o fatorial: "))
fat = 1
for i in range(n, 0, -1):
    fat *= i
print(f"{n}! = {fat}")
