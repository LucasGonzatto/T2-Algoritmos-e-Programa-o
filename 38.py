ano = 1995
salario = 1000
aumento = 1.5 / 100
anoatual = int(input("Digite o ano atual: "))
for i in range(1996, anoatual + 1):
    salario += salario * aumento
    aumento *= 2
print("Salário atual:", round(salario, 2))
