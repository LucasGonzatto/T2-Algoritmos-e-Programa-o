while True:
    popa = int(input("Informe a população do país A: "))
    popb = int(input("Informe a população do país B: "))
    taxaA = float(input("Informe a taxa de crescimento de A (%): "))
    taxaB = float(input("Informe a taxa de crescimento de B (%): "))
    if popa > 0 and popb > 0 and taxaA > 0 and taxaB > 0:
        anos = 0
        while popa < popb:
            popa += popa * (taxaA / 100)
            popb += popb * (taxaB / 100)
            anos += 1
        print("Levará", anos, "anos para A ultrapassar ou igualar B.")
    else:
        print("Dados inválidos.")
    repetir = input("Deseja repetir? (s/n): ").lower()
    if repetir != 's':
        break
