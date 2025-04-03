class ContaBancaria:
    def __init__(self, titular, saldo, limite):
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_titular(self): return self.__titular
    def get_saldo(self): return self.__saldo
    def set_limite(self, novo_limite): self.__limite = novo_limite

    def depositar(self, valor):
        if valor > 0: self.__saldo += valor
        else: print("Valor inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo + self.__limite: self.__saldo -= valor
        else: print("Saldo insuficiente.")

# Testando a classe
conta1 = ContaBancaria("Rafinha", 1000.0, 500.0)

# Interações
print(f"Titular: {conta1.get_titular()} - Saldo: R${conta1.get_saldo():.2f}")
conta1.set_limite(float(input("Novo limite: ")))

conta1.depositar(float(input("Depósito: ")))
conta1.sacar(float(input("Saque: ")))

print(f"Saldo final: R${conta1.get_saldo():.2f}")
