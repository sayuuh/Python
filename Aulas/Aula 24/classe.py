import datetime                          #python (ler mais)
from random import randint 
from time import sleep

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome 
        self.__preco = preco 
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    def listarProduto(self):
        print('---' * 10)
        print(f'Produto: {self.nome}')
        print(f'Preço: R$ {self.preco}')
        print('---' * 10)

class CarrinhoCompra:
    def __init__(self):
        self.__produtos = []
        # self.__data = datetime.datetime.now() -> coloca data e horário completo
        self.__data = datetime.date.today()
        self.__codigo = self.gerar_codigo()

    @staticmethod
    def gerar_codigo():
        return randint(99999, 9999999)

    def adicionar_produto(self, produto):
        self.__produtos.append(produto)

    def listar_produtos(self):
        print('---' * 10)
        for produto in self.__produtos:
            print(f'{produto.nome} ... R$ {produto.preco}')
        print('---' * 10)

    def calcular_compra(self):
        total = 0
        for produto in self.__produtos:
            total += produto.preco
        return total

    def finalizar_compra(self):
        print('---' * 15)
        print('      *** CUPOM FISCAL ***')
        print('---' * 15)
        sleep(2)
        print(f'Codigo ......... {self.__codigo}')
        print(f'Data   ......... {self.__data}')
        print('---' * 15)
        sleep(1)
        for i, produto in enumerate(self.__produtos):
            print(f'{i+1} - {produto.nome} ....... R$ {produto.preco}')
            sleep(1)
        print('---' * 15)
        print(f'Total ............................ R$ {self.calcular_compra()}')
        print('---' * 15)
        sleep(3)
        print('      *** OBRIGADO, VOLTE SEMPRE! ***')
        print('---' * 15)
        self.limpar_array()

    def limpar_array(self):
        self.__produtos = []