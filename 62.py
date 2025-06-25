texto = input("Digite uma palavra ou frase: ").lower()
texto = ''.join(c for c in texto if c.isalnum())
print("É palíndromo?", texto == texto[::-1])
