from funcionario import Gerente, Vendedor
from endereco import *


est1 = Estado('Estado 1', 'SG')
cid1 = Cidade('Cidade 1', est1)
end1 = Endereco('Rua do End 1', 12, 'Bairro Nobre', '12365-789', cid1)

g = Gerente('Gerente Nome Completo', '15/02/1995', '123.654.987-74', end1)
print(g.enderecos.listar())
g.getSalario()



est2 = Estado('São Paulo', 'SP')
cid2 = Cidade('São Paulo', est2)
end2 = Endereco('Av Paulista', 19, 'Centro', '11365-789', cid2)
v = Vendedor('Vendedor Nome Completo', '05/11/1987', '144.789.652-87', end2)
print(v.enderecos.listar())
print(round(v.getsalario(), 2))
print(v.equipe)