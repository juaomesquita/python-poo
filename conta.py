class Conta:
    def __init__(self, conta, cliente, saldo, limite):
        self.__conta = conta
        self.__cliente = cliente
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do cliente {} é: R${:.2f}".format(self.cliente, self.saldo))

    def deposisita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if self.pode_sacar(valor):
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
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def titular(self, cliente):
        self.__cliente = cliente

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo


    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}

    def __str__(self):
        return f"Conta: {self.conta}\n{self.cliente}\nSaldo: R${self.saldo:.2f}\nLimite: {self.limite:.2f}"
