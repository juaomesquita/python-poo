class Conta:
    def __init__(self, conta, titular, saldo, limite):
        self.__conta = conta
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do cliente {} é: R${:.2f}".format(self.__titular, self.__saldo))

    def deposisita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if valor <= (self.__saldo + self.__limite):
            self.__saldo -= valor
        else:
            print("O valor R${:.2f} passou o limite.".format(valor))

    def transfere(self, conta, valor):
        self.saca(valor)
        conta.deposisita(valor)

    #conta titular saldo limite

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def titular(self):
        return self.__titular.title()

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite