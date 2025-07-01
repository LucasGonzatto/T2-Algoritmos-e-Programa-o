menu = {
    100: ("Cachorro Quente", 1.20),
    101: ("Bauru Simples", 1.30),
    102: ("Bauru com ovo", 1.50),
    103: ("Hambúrguer", 1.20),
    104: ("Cheeseburguer", 1.30),
    105: ("Refrigerante", 1.00)
}
total = 0
while True:
    cod = int(input("Digite o código do item (0 para sair): "))
    if cod == 0:
        break
    if cod in menu:
        qtd = int(input("Quantidade: "))
        nome, preco = menu[cod]
        valor = qtd * preco
        print(f"{nome}: R$ {valor:.2f}")
        total += valor
    else:
        print("Código inválido.")
print("Total do pedido: R$", total)
