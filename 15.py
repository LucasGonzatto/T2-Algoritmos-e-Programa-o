n = int(input("Quantos termos da série Fibonacci você quer ver? "))
a = 1
b = 1
print(a, b, end=' ')
for i in range(n - 2):
    proximo = a + b
    print(proximo, end=' ')
    a, b = b, proximo
print()
