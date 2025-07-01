while True:
    nome = input("Digite seu nome: ")
    if len(nome) > 3:
        break
    print("O nome deve ter mais de 3 caracteres.")
while True:
    idade = int(input("Digite sua idade: "))
    if 0 <= idade <= 150:
        break
    print("Idade inválida.")
while True:
    salario = float(input("Digite seu salário: "))
    if salario > 0:
        break
    print("Salário deve ser maior que zero.")
while True:
    sexo = input("Digite seu sexo (f/m): ").lower()
    if sexo in ['f', 'm']:
        break
    print("Sexo inválido.")
while True:
    civil = input("Digite seu estado civil (s, c, v, d): ").lower()
    if civil in ['s', 'c', 'v', 'd']:
        break
    print("Estado civil inválido.")
