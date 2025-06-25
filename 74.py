def fatorialiterativo(n):
    if n < 0:
        return "Erro"
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat
def fatorialrecursivo(n):
    if n < 0:
        return "Erro"
    if n == 0 or n == 1:
        return 1
    return n * fatorialrecursivo(n - 1)
n = int(input("Digite um número: "))
print("Iterativo:", fatorialiterativo(n))
print("Recursivo:", fatorialrecursivo(n))