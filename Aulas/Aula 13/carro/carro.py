from turtle import Turtle


class Carro:
    def __init__(self, nome1, cor1, placa1, ligado=False, andando=False):
        self.nome = nome1
        self.cor = cor1
        self.placa = placa1
        self.ligado = ligado
        self.andando = andando
    
    def ligar_carro(self):
        if self.ligado:
            return print(f'{self.nome} já estou ligado') 
        self.ligado = True
        print(f'{self.nome} ligado')
    
    def desligar_carro(self):
        if not self.ligado:
            return print(f'{self.nome} já está desligado')
        if self.andando:
            return print(f'{self.nome} está andando')
        self.ligado = False
        print(f'{self.nome} desligado')

    def andar(self):
        if not self.ligado:
            return print(f'{self.nome} está desligado')
        self.andando = True
        print(f'{self.nome} andou')

    def parar_carro(self):
        if not self.andando:
            return print(f'{self.nome} já está parado')
        self.andando = False
        print(f'{self.nome} parou')


# pass = serve para "passar" e não dar erro no codigo quando não tem nada dentro da função 

