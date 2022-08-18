class Funcionario:
    __valor_hora_cargo = [189.56, 86.05, 35.48]
    __nome_cargo = ['Diretor', 'Gerente', 'Vendedor']

    def __init__(self, nome, cargo, horas_trabalhadas, salario):
        self.nome = nome
        self.cargo = cargo
        self.horas_trabalhadas = horas_trabalhadas
        self.salario = salario

    def exibir_funcionario(self):
        print(f'NOME: {self.nome}')
        print(f'CARGO: {self.__nome_cargo[self.cargo]}')
        print(f'HORAS TRABALHADAS: {self.horas_trabalhadas} horas')
        print(f'SALARIO: R$ {self.salario}')

    def adicionar_horas_trabalhadas(self):
        self.horas_trabalhadas += 1

    def calcular_salario(self):
        self.salario = self.horas_trabalhadas * self.__valor_hora_cargo[self.cargo]

    @classmethod
    def alterar_salario_funcionarios(cls, indice, valor):
        cls.__valor_hora_cargo[indice] = valor

    @classmethod # decorador
    def retornar_cargos(cls):
        return cls.__nome_cargo




fun = Funcionario('Sayumi', 1, 10, 2000)
print(fun.exibir_funcionario())
fun.adicionar_horas_trabalhadas()
fun.adicionar_horas_trabalhadas()
fun.adicionar_horas_trabalhadas()
print(fun.exibir_funcionario())