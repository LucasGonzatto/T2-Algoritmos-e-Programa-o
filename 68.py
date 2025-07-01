def calculadora(a, b, op):
    if op == 'soma':
        return a + b
    elif op == 'subtracao':
        return a - b
    elif op == 'multiplicacao':
        return a * b
    elif op == 'divisao':
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Operação inválida"
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
op = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ")
print("Resultado:", calculadora(a, b, op))
