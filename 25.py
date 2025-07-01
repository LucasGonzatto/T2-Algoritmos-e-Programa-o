qtd = int(input("Quantas pessoas? "))
soma = 0
for i in range(qtd):
    idade = int(input(f"Idade da {i+1}ª pessoa: "))
    soma += idade
media = soma / qtd
print("Média de idade:", media)
if media <= 25:
    print("Turma jovem")
elif media <= 60:
    print("Turma adulta")
else:
    print("Turma idosa")
