# Jogo da Forca 
# Criei uma lista de palavras pro jogo
# LISTA OU VETOR

from random import randint 
palavras = ['Casa', 'Carro', 'Aviao', 'Moto', 'Mesa', 'Cadeira', 'Teto', 'Casarao', 'Terreno', 'Escola', 'Curso', 'Musica', 'Montanha', 'Piscina', 'Pia', 'Porto', 'Pa', 'Padaria', 'Empresa', 'Ilha', 'Televisao', 'Radio', 'Rua', 'Planta', 'Arvore', 'Portao', 'Computador', 'Escada', 'Sofa']

indice = " "
palavra_secreta = " " 
tentativa = []
chutes = []


def exibirMsg(msg):
    print(msg)

def encontraLetra(chute):
    temLetra = False
    for i, letra in enumerate(palavra_secreta):
        if(chute.upper() == letra.upper()):
            tentativa[i] = chute.upper()
            temLetra = True
    return temLetra      

def jogar():
    tentativas = 5
    while(True):
        chute = input('Digite uma letra: ')
        if(encontraLetra(chute)):
            exibirMsg(tentativa)
        else:
            exibirMsg(f'Letra {chute} não encontrada')
            chutes.append(chute.upper())
            exibirMsg(chutes)
            tentativas -= 1
            exibirMsg(f'Restam {tentativas} tentativas')
            exibirMsg(tentativa)

        if(verificaVitoria()):
            exibirMsg('PARABÉNS, VOCÊ VENCEU')
            break

        if(tentativas <= 0):
            exibirMsg('VOCÊ PERDEU, \n JOGUE NOVAMENTE')
            exibirMsg(f'A palavra secreta é {palavra_secreta.upper()}!!')
            break

def verificaVitoria():
    if( '_' in tentativa):
        return False
    else:
        return True

def iniciaJogo():
    global indice
    indice = randint(0, len(palavras) - 1) # Recebe um numero aleatorio entre 0 e a quantidade total de palavras
    global palavra_secreta 
    palavra_secreta = palavras[indice] # palavra do jogo 
    global tentativa
    tentativa = []
    global chutes
    chutes = []

    for i in range(len(palavra_secreta)):
        tentativa.append('_')
   

def escolha():
    while(True): # continuar == True
        iniciaJogo()
        exibirMsg('**** JOGO DA FORCA ****')
        menu = int(input(' 1 - Jogar \n 2 - Sair \n R: '))
        if(menu == 1):
            jogar()
        else:
            exibirMsg('Até logo!')
            break

escolha()