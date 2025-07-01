n = int(input("Digite um número: "))
divisoes = 0
for i in range(2, n + 1):
    primo = True
    for j in range(2, i):
        divisoes += 1
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i, end=' ')
print("\nNúmero de divisões realizadas:", divisoes)
