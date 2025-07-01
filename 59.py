texto = input("Digite uma frase: ").lower()
vogais = 'aeiou'
cont_vogais = cont_consoantes = 0
for letra in texto:
    if letra.isalpha():
        if letra in vogais:
            cont_vogais += 1
        else:
            cont_consoantes += 1
print("Vogais:", cont_vogais)
print("Consoantes:", cont_consoantes)
