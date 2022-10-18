# JOGO DA VELHA 

'''    0   1   2
   0 [ 1 , 2 , 3 ]
   1 [ 4 , 5 , 6 ]
   2 [ 7 , 8 , 9 ]
   LINHA 
   x x x 
   COLUNA
   x
   x
   x
   DIAGONAL
   x [0,0] == [1,1] == [2,2]
    x
     x
      x[0,2] == [1,1] == [2,0]
    x
  x
'''

tabuleiro = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

board = []
cont = 1

for i in range(3):
    b = []
    for j in range(3):
        b.append(cont)
        cont += 1
    board.append(b[:])

def listar_tabuleiro():
    for i in tabuleiro:
        print(i)

def pergunta_jogada():
    while True:
        jogada = int(input('Onde deseja Jogar? '))
        if verifica_vazio(jogada):
            return jogada

def verifica_vazio(valor):
    for i in tabuleiro:
        for j in i:
            if j == valor:
                return True
    return False

def verificaVitoria():
    # linhas 
    for i in range(len(tabuleiro)):
        if(tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][0] == tabuleiro[i][2]):
            return True

        if(tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[0][i] == tabuleiro[2][i]):
            return True

    if(tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[0][0] == tabuleiro[2][2]):
        return True

    if(tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[0][2] == tabuleiro[2][0]):
        return True

    return False

def alterar_campo(valor, letra):
    for i in range(len(tabuleiro)):
        if tabuleiro[i][0] == valor:
            tabuleiro[i][0] = letra
        elif tabuleiro[i][1] == valor:
            tabuleiro[i][1] = letra
        elif tabuleiro[i][2] == valor:
            tabuleiro[i][2] = letra

jogadas = 0

while True:
    listar_tabuleiro()
    if(jogadas % 2 == 0):
        print("jogador 1")
        alterar_campo(pergunta_jogada(), "X")
        if verificaVitoria():
            print('Jogador 1 Ganhou a Partida! PARABÉNS!!!')
            break

    else:
        print('Jogador 2')
        alterar_campo(pergunta_jogada(), "O")
        if verificaVitoria():
            print('Jogador 2 Ganhou a Partida! PARABÉNS!!!')
            break
    
    jogadas += 1
    if jogadas == 9:
        print('Deu velha!')
        break

''' 
    CASA 
    1 - Gerar menu inicial do jogo. (1 - JOGAR 2 - SAIR)
    2 - Ao iniciar a primeira partida perguntar o nome do JOGADOR 1 e do JOGADOR 2
    3 - Gerar placar da partida toda vez que o jogo finalizar/iniciar -> ( NOME 1 x 5 NOME)
'''