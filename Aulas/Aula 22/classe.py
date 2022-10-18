from random import randint

class Pessoa:
    def __init__(self, nome, sexo, telefone, endereco):
        self.__codigo = self.gerar_codigo()
        self.nome = nome
        self.sexo = sexo
        self.telefone = telefone
        self.endereco = endereco 

    @staticmethod
    def gerar_codigo():
        return randint(10000, 9999999)
    
    def atualizar_endereco(self, valor):
        self.endereco = valor 
    
    def atualizar_telefone(self, valor):
        self.telefone = valor
    
    def listar_pessoa(self):
        print('____' * 5)
        print(f'  CODIGO: {self.__codigo}')
        print(f'    NOME: {self.nome}')
        print(f'    SEXO: {self.sexo}')
        print(f'TELEFONE: {self.telefone}')
        print(f'ENDERECO: {self.endereco}')
        print('____' * 5)

class Cliente(Pessoa):
    pass

class Funcionario(Pessoa):
    def __init__(self, nome, sexo, telefone, endereco, horasTrabalhadas):
        super().__init__(nome, sexo, telefone, endereco)
        self.horas_trabalhadas = horasTrabalhadas
        self.__salario = 0

    def listar_pessoa(self):
        super().listar_pessoa()
        print(f'   HORAS: {self.horas_trabalhadas}')
        print(f' SALÁRIO: R$ {self.__salario}')
        print('____' * 5)

    def adicionar_horas_trabalhadas(self, valor):
        self.horas_trabalhadas += valor

    def calcular_salario(self):
        self.__salario = round(self.horas_trabalhadas * 25.43, 2)

c = Cliente('Akio Hashimoto', 'Masculino', '2198654321', 'Rua tal')
c.listar_pessoa()


f  = Funcionario('Pedrinho J', 'M', '12987654321', 'Rua aga, 45', 128)
f.adicionar_horas_trabalhadas(16)
f.calcular_salario()
f.listar_pessoa()


p = Pessoa('Maria', 'F', '32987564', 'Rua pe, 45')
p.listar_pessoa()