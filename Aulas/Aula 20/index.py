from random import randint
class Produto:
    variavelDeClasse = 'Produto'
    def __init__ (self):
        self._codigo = self.__gerarCodigoProduto()
        self._nome = ''
        self._preco = 0

    
    def listarProduto(self):
        print('-' * 15)
        print('PRODUTO')
        print(f' COD: {self._codigo} \nNOME: {self._nome} \n  R$: {self._preco}')
        print('-' * 15)

    @classmethod
    def metodoDeClasse(cls):
        print(cls.variavelDeClasse)

    @staticmethod
    def __gerarCodigoProduto():
        return randint(10000, 99999)
 

    #  METODOS ASSESSORES 
    #     GET / GETTERS 

    @property #DECORADOR 
    def nome(self):
        return self._nome 

    @property
    def preco(self):
        return f"R$ {self._preco}" # R$ 0 -> = 0

    #  METODOS MODIFICADORES 
    #     SET / SETTERS 

    @nome.setter
    def nome(self, valor):
        self._nome = valor.strip()

    @preco.setter
    def preco(self, valor):
        print(valor)
        valor = valor.replace('R$','')
        valor = valor.replace(',','.')
        valor = valor.strip()
        #       ' 25,89 ' -> '25,89'
        #  25.89 -> 2589
        if valor.replace('.', '').isnumeric():
            self._preco = float(valor) 
        else:
            self._preco = 0 
            print('ERROR: Digite um valor válido')

p = Produto()

print('=== MERCADINHO DINHO ===')
while(True):
    menu = input('1 - Cadastrar Produto \n2 - Listar Produto \n3 - Sair \nR: ')
    if menu == '1':
        p.nome = input('Digite o nome do produto: ')
        while(True):
            p.preco = input('Digite o preço do produto: ')
            if p.preco != 'R$ 0':
                print('Produto Cadastrado com sucesso!')
                break
    elif menu == '2':
        p.listarProduto()
    else:
        print('Finalizando Programa. . . ')
        break



p.listarProduto()