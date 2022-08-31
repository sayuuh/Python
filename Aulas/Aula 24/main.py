from classe import Produto, CarrinhoCompra

agua = Produto('Água 500ml', 2.50)
cerveja = Produto('Skol 350ml', 4.00)
refrigerante = Produto('Guaraná 2L', 3.50)
# agua.listarProduto()

cc = CarrinhoCompra()
cc.adicionar_produto(agua)
cc.adicionar_produto(cerveja)
cc.adicionar_produto(refrigerante)
cc.finalizar_compra()
cc.listar_produtos()