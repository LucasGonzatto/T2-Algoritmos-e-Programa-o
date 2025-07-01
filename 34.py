n = int(input("Digite um número: "))
primo = True
for i in range(2, n):
    if n % i == 0:
        primo = False
        break
print("É primo" if primo and n > 1 else "Não é primo")
