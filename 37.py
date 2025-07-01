maisalto = maismagro = None
maisbaixo = maisgordo = None
somaaltura = somapeso = 0
cont = 0
while True:
    cod = input("Digite o código do cliente (0 para sair): ")
    if cod == '0':
        break
    altura = float(input("Altura (m): "))
    peso = float(input("Peso (kg): "))
    if maisalto is None or altura > maisalto[1]:
        maisalto = (cod, altura)
    if maisbaixo is None or altura < maisbaixo[1]:
        maisbaixo = (cod, altura)
    if maisgordo is None or peso > maisgordo[1]:
        maisgordo = (cod, peso)
    if maismagro is None or peso < maismagro[1]:
        maismagro = (cod, peso)
    somaaltura += altura
    somapeso += peso
    cont += 1
print("Mais alto:", maisalto)
print("Mais baixo:", maisbaixo)
print("Mais gordo:", maisgordo)
print("Mais magro:", maismagro)
print("Média altura:", somaaltura / cont)
print("Média peso:", somapeso / cont)
