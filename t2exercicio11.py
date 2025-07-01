a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a > b:
    a, b = b, a
soma = 0
for n in range(a + 1, b):
    print(n, end=' ')
    soma += n
print("\nSoma dos números:", soma)
