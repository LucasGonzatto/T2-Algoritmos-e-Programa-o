maisalto = maisbaixo = None
for i in range(10):
    num = int(input("Número do aluno: "))
    altura = float(input("Altura em cm: "))
    if maisalto is None or altura > maisalto[1]:
        maisalto = (num, altura)
    if maisbaixo is None or altura < maisbaixo[1]:
        maisbaixo = (num, altura)
print("Mais alto:", maisalto)
print("Mais baixo:", maisbaixo)
