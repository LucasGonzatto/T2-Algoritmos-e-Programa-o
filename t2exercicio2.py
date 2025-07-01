while True:
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")
    if nome == senha:
        print("Erro: A senha não pode ser igual ao nome do usuário.")
    else:
        print("Cadastro realizado com sucesso.")
        break
