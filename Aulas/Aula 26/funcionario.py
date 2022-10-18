from random import randint


class Funcionario:
    def __init__(self, nome, nascimento, cpf, endereco):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__cpf = cpf
        self.__enderecos = endereco

    @property
    def nome(self):
        return self.__nome

    @property
    def nascimento(self):
        return self.__nascimento

    @property
    def cpf(self): 
        return self.__cpf

    @property
    def enderecos(self):
        return self.__enderecos

class Gerente(Funcionario):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(nome, nascimento, cpf, endereco)

    @staticmethod
    def getSalario():
        print('Salário: R$ 7.589,58')

class Vendedor(Funcionario):
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(nome, nascimento, cpf, endereco)
        self.__equipe = EquipeVenda()


    @staticmethod
    def getsalario():
        return randint(100, 5000) + 1178.56

    @property
    def equipe(self):
        return self.__equipe.nome

class EquipeVenda:
    def __init__(self):
        self.__nome = 'Equipe Alpha'

    @property
    def nome(self):
        return self.__nome