def vddemail(email):
    if email.count('@') != 1:
        return False
    parte1, parte2 = email.split('@')
    if len(parte1) < 1:
        return False
    if '.' not in parte2:
        return False
    dominio, *resto = parte2.split('.')
    if len(dominio) < 1 or len(resto[-1]) < 2:
        return False
    return True
email = input("Digite um e-mail: ")
print("Válido:", vddemail(email))
