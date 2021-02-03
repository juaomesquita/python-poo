class Cliente:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascmento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def __str__(self):
        return "Cliente: {} {}".format(self.__nome, self.__sobrenome)
