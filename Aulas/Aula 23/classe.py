from random import randint
import re
class Editora:
    def __init__(self):
        self.__codigo = self.gerarCodigo()
        self.__razaoSocial = ''
        self.__email = ''
        self.__telefone = ''

    @property
    def codigo(self):
        return f'Codigo: {self.__codigo}'
            
    @property
    def razaoSocial(self):
        return f'Nome: {self.__razaoSocial}'

    @razaoSocial.setter
    def razaoSocial(self, valor):
        self.__razaoSocial = valor

    @property
    def email(self):
        return f'Email: {self.__email}'

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def telefone(self):
        return f'Telefone: {self.__telefone}'

    @telefone.setter
    def telefone(self, valor):
        self.__telefone = valor
            

    def listarEditora(self):
        print('==' * 10)
        print(self.codigo)
        print(self.razaoSocial)
        print(self.email)
        print(self.telefone)
        print('==' * 10)

    @staticmethod
    def gerarCodigo():
        return randint(1, 9999) + randint(10, 50)

class Livro:
    def __init__(self, titulo, idioma):
        self.__codigo = self.gerarCodigo()
        self.__titulo = titulo
        self.__idioma = idioma
        self.__editora = ''

    @staticmethod
    def gerarCodigo():
        return randint(10000, 99999)

    def listarLivro(self):
        print('***' * 10)
        print(f'Codigo: {self.codigo}')
        print(f'Titulo: {self.titulo}')
        print(f'Idioma: {self.idioma}')
        print(f'Editora: {self.editora}')
        print('***' * 10)

    # get and Set

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def idioma(self):
        return self.__idioma

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, valor):
        self.__editora = valor