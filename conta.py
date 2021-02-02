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
        self.__saldo -= valor

    def transfere(self, conta, valor):
        self.saca(valor)
        conta.deposisita(valor)

    #conta titular saldo limite

    def get_conta(self):
        return self.__conta

    def set_conta(self, conta):
        self.__conta = conta

    def get_titular(self):
        return self.__titular

    def set_titular(self, titular):
        self.__titular = titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite