class ContaBancaria:
    def __init__(self, conta):
        self.conta = conta
        self.saldo = 0.0
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")
