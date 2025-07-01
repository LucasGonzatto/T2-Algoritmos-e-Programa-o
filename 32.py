n = int(input("Fatorial de: "))
fat = 1
print(f"{n}! =", end=' ')
for i in range(n, 0, -1):
    fat *= i
    print(i, end=' ' if i == 1 else '. ')
print(f"= {fat}")
