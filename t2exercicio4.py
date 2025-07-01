a = 80000
b = 200000
anos = 0
while a < b:
    a += a * 0.03
    b += b * 0.015
    anos += 1
print("Levará", anos, "anos para a população de A passar ou igualar a de B.")
