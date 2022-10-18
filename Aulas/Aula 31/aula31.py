# MANIPULANDO ARQUIVOS
# .txt 

'''
    r -> Ler
    w -> Escrever
    a -> Acrescentar
    r+ -> Ler e acrescentar 
'''

caminho = './Aulas/Aula 31'

# escrever
'''with open(f'{caminho}/teste.txt', 'w') as arquivo:
    arquivo.write('Hello, World')'''

# acrescentar
'''with open(f'{caminho}/teste.txt', 'a') as arquivo:
    arquivo.write('\n Posso escrever o que eu quiser!')'''

# Ler
'''with open(f'{caminho}/teste.txt', 'r') as arquivo:
    texto = []
    for linha in arquivo:
        texto.append(linha)
    texto[0] = 'Linha 1\n'
    print(texto)'''

# for i in texto: <- apenas exibindo o que tem na lista     
#  print(i)


'''with open(f'{caminho}/teste.txt', 'w') as arquivo:
    for i in texto:
        print(i)'''

# Ler e acrescentar 

with open(f'{caminho}/teste.txt', 'r+') as arquivo:
    for i in arquivo:
        print(i)
    arquivo.write('Linha 4\n')