qtd=int(input("Quantas notas? "))
soma=0
for i in range(qtd):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    soma += nota
media=soma / qtd
print("Média das notas:", media)
