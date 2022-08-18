from random import randint
class Produto:
    lista_tipos = ['Alimentação', 'Limpeza', 'Pets']

    # Inicializando classe / criando objeto
    def __init__(self, codigo, nome, preco, qntEstoque, tipo):
        self.codigo = self.gerarCodigoProduto()
        self.nome = nome
        self.preco = preco
        self.qntEstoque = qntEstoque
        self.tipo = tipo

    def listarProduto(self):
        print(f'Codigo: {self.codigo}')
        print(f'Nome: {self.nome}')
        print(f'R$ {self.preco}')
        print(f'Qnt Estoque: {self.qntEstoque}')
        print(f'Tipo: {self.retornarTipo(self.tipo)}')
        print('--' * 15)

    def valorEstoque(self):
        return print(f'Total do estoque R$ {self.preco * self.qntEstoque}')

    def venderProduto(self, qnt):
        if qnt > self.qntEstoque:
            return print('Quantidade em estoque insuficiente!')
        self.qntEstoque -= qnt
        self.listarProduto()
        print(f'Venda realizada com sucesso! Restam {self.qntEstoque} produtos em estoque')
        self.verificarComprarMais(self.qntEstoque)

    @classmethod # puxa apenas pela classe
    def listarTipos(cls):
        print(cls.lista_tipos)

    @classmethod
    def retornarTipo(abacate, tipo):
        return abacate.lista_tipos[tipo - 1]

    @staticmethod # não recebe classe, nem instancia pra funcionar
    def verificarComprarMais(qnt):
        if qnt < 5:
            print('Compre mais produtos')
        else:
            print('Ainda há produtos no estoque')

    @staticmethod # não recebe classe, nem instancia pra funcionar
    def gerarCodigoProduto():
        return randint(10000, 99999)

