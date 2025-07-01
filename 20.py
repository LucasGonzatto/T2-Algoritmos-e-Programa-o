while True:
    n = int(input("Digite um número (0 a 15) para calcular o fatorial: "))
    if 0 <= n < 16:
        fat = 1
        for i in range(n, 0, -1):
            fat *= i
        print(f"{n}! = {fat}")
    else:
        print("Número fora do limite.")
    sair = input("Deseja calcular outro? (s/n): ").lower()
    if sair != 's':
        break
