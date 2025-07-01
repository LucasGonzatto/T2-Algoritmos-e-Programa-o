gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
maior = menor = soma = 0
alunos = 0
while True:
    acertos = 0
    for i in range(10):
        resp = input(f"Resposta da questão {i+1}: ").upper()
        if resp == gabarito[i]:
            acertos += 1
    print("Acertos:", acertos)
    soma += acertos
    alunos += 1
    if maior < acertos:
        maior = acertos
    if alunos == 1 or acertos < menor:
        menor = acertos
    cont = input("Outro aluno vai usar o sistema? (s/n): ").lower()
    if cont != 's':
        break
print("Maior acerto:", maior)
print("Menor acerto:", menor)
print("Total de alunos:", alunos)
print("Média da turma:", soma / alunos)
