maior = menor = None
soma_veic = soma_acid = cont_cid2000 = 0
for i in range(5):
    cod = input("Código da cidade: ")
    veic = int(input("Número de veículos: "))
    acid = int(input("Número de acidentes: "))
    if maior is None or acid > maior[1]:
        maior = (cod, acid)
    if menor is None or acid < menor[1]:
        menor = (cod, acid)
    soma_veic += veic
    if veic < 2000:
        soma_acid += acid
        cont_cid2000 += 1
print("Maior índice:", maior)
print("Menor índice:", menor)
print("Média de veículos:", soma_veic / 5)
print("Média de acidentes nas cidades < 2000 veículos:", soma_acid / cont_cid2000 if cont_cid2000 else 0)
