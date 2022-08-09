from conta import Conta
from cliente import Cliente


print('-' * 15)
print('BANCO DOS BANCOS')
print('-' * 15)

cliente1 = Cliente('Sayumi Souza', '123.456.789-13')
conta1 = Conta(cliente1, 1000)

print(conta1.titular.nome)
print(conta1.titular.cpf)

'''
print(cliente1.nome)
print(cliente1.cpf)

print(cliente1)
print(conta1.titular)
'''

if(conta1.sacar(500)):
    print('Saque efetuado com sucesso')
else:
    print('Saldo insuficiente')                        


cliente2 = Cliente('Kenji Ernesto', '789.456.123-45')
conta2 = Conta(cliente2, 1000, 3000.0)

if(not conta2.transferir(conta1, 150)):
    print('Saldo em conta insuficiente para realizar a transferencia')
else:
    print('Transferencia efetuada com sucesso')

conta2.extrato()
conta1.extrato()

