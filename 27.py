turmas = int(input("Quantas turmas? "))
total = 0
for i in range(turmas):
    while True:
        alunos = int(input(f"Quantidade de alunos na turma {i+1}: "))
        if alunos <= 40:
            break
        print("Turma não pode ter mais de 40 alunos.")
    total += alunos
media = total / turmas
print("Média de alunos por turma:", media)
