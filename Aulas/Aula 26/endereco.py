class Endereco:
    def __init__(self, rua, numero, bairro, cep, cidade):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cep = cep
        self.__cidade = cidade

    @property
    def rua(self):
        return self.__rua

    @property
    def numero(self):
        return self.__numero

    @property
    def bairro(self):
        return self.__bairro

    @property
    def cep(self):
        return self.__cep
        
    @property
    def cidade(self):
        return self.__cidade

    def listar(self): # void : String
        return f'{self.rua}, nº {self.numero}, {self.bairro}, {self.cidade.nome} -  {self.cidade.estado.sigla}'
    
    


class Cidade:
    def __init__(self, nome, estado):
        self.__nome = nome
        self.__estado = estado

    @property
    def nome(self):
        return self.__nome

    @property
    def estado(self):
        return self.__estado

class Estado:
    def __init__(self, nome, sigla):
        self.__nome = nome 
        self.__sigla = sigla

    @property
    def nome(self):
        return self.__nome

    @property
    def sigla(self):
        return self.__sigla