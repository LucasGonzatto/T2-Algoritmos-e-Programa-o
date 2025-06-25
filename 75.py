def sao_anagramas(p1, p2):
    p1 = ''.join(sorted(p1.lower().replace(' ', '')))
    p2 = ''.join(sorted(p2.lower().replace(' ', '')))
    return p1 == p2
a = input("Palavra 1: ")
b = input("Palavra 2: ")
print("São anagramas?", sao_anagramas(a, b))
