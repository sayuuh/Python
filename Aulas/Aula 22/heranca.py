''' 
    Atributos
        Endereco, Codigo, Nome, Telefone e Sexo
    Metodos
        gerarCodigo, atualizarTelefone, atualizarEndereco, listar
    Pessoas 
        Codigo, Nome, Sexo, Endereco, Telefone 
    Metodos
        geraCodigo, atualizarTelefone, atualizarEndereco, listar
'''



class SerHumano:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def falar(self):
        return print(f'{self.nome}:')

    def listar(self):
        print(f'NOME: {self.nome}')
        print(f' CPF: {self.cpf}')

class Cliente(SerHumano):
    def comprar(self):
        return print(f'{self.nome} está comprando')

    def falar(self):
        super().falar()
        return print(f'- Desejo levar este produto')

class Funcionario(SerHumano):
    def vender(self):
        return print(f'{self.nome} está vendendo')

    def falar(self):
        super().falar()
        return print(f'- Débito ou Crédito?')

c = Cliente('Gabriel', '11111111111111')
c.falar()

f = Funcionario('Jorge', '000000000000')
f.falar()