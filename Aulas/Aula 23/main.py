from classe import Editora
from classe import Livro

editora = Editora()
print(editora.codigo)
editora.razaoSocial = "Safaria"
editora.email = 'contato@safaria.com.br'
editora.telefone = '21989898989'
editora.listarEditora()

livro = Livro('O titulo', 'pt-br')
livro.editora = editora
print(livro.editora.codigo)
print(livro.editora.razaoSocial)
print(livro.editora.email)
print(livro.editora.telefone)
print(livro.editora.gerarCodigo())
livro.editora.listarEditora()

livro.listarLivro()