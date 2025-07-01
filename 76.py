def destriangulo(alt, tipo):
    for i in range(1, alt + 1):
        if tipo == 'esquerda':
            print('*' * i)
        elif tipo == 'direita':
            print(' ' * (alt - i) + '*' * i)
        elif tipo == 'centralizado':
            print(' ' * (alt - i) + '*' * (2 * i - 1))
a = int(input("Altura do triângulo: "))
t = input("Tipo (esquerda, direita, centralizado): ").lower()
destriangulo(a, t)
