from wsgiref.validate import validator


class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def sacar(self, valor):
        if self.saldo < valor:
            return print(f'{self.numero} tem saldo insuficiente')
        self.saldo -= valor
        print('Saque efetuado com sucesso')

    def depositar(self, valor):
        self.saldo += valor
        print('Depósito efetuado com sucesso')

    def extrato(self):
        print(f'{self.numero} de {self.titular} tem saldo de R$ {self.saldo}')

    def gerar_numero_conta(self):
        

