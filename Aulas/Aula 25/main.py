from banco import Cliente, Conta

c1 = Cliente("Matheus F.", "123.654.987-96")
cc1 = Conta(4321, 100, c1)

c2 = Cliente("Kenji.", "123.987.456-15")
cc2 = Conta(1234, 50, c2)

cc1.sacar(50)
cc1.transferir(cc2, 20)
cc1.depositar(155)
cc1.transacoes()
cc1.listar_conta()

cc2.depositar(50)
cc2.sacar(150)
cc2.listar_conta()

del cc1
print(' ******* FIM  *******')
print('\n' * 5)