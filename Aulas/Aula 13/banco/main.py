from conta import Conta

conta1 = Conta('1234-5', 'Akio', 1000, 5000)
print('-' * 15)
print('BANCO DOS BANCOS')
print('-' * 15)


conta1.depositar(500)
conta1.sacar(1500)
conta1.extrato()


conta2 = Conta('4321-0', 'Kenji', 1000, 3000)
conta2.extrato()




