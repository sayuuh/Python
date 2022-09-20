from cProfile import label
from tkinter import *

telaInicial = Tk() # instanciar 

telaInicial['bg'] = 'black' # alterar a cor de fundo
telaInicial.title('Minha Primeira Tela') # alterar título


largura = 850 # altura do programa
altura = 650 # largura do programa
larguraUser = telaInicial.winfo_screenwidth()
alturaUser = telaInicial.winfo_screenheight()
print(larguraUser, alturaUser) # tela do usuário
larguraX = int((larguraUser - largura)/2)
alturaY = int((alturaUser - altura)/2)
telaInicial.geometry(f'{largura}x{altura}+{larguraX}+{alturaY}')
telaInicial.resizable(True, True) 
telaInicial.minsize(850, 650)
telaInicial.maxsize(1440, 900)
# telaInicial.state('zoomed') # inicializa zoomed(maximizado) / iconic(minimizado)

def entrar():
    # print('Olá, Mundo!')
    labelMsg.config(text='Olá, Mundo!')
    
btnEntrar = Button(telaInicial, text='Entrar', command=entrar) # cria a instancia iniciar 
btnEntrar.pack() # mostra o botão 

labelMsg = Label(telaInicial, text='')
labelMsg.pack()

# ultima linha 
telaInicial.mainloop() # abre a tela 




# () = metodo
# [] = atributo