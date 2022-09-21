from tkinter import *

# Funções
def verficaValores():
    if len(txtNum1.get().strip()) < 1 or not txtNum1.get().strip().isnumeric() and len(txtNum2.get().strip()) < 1 or not txtNum2.get().strip().isnumeric() :
        return False
    return True

def somar():
        if verficaValores():
            num1 = int(txtNum1.get().strip())
            num2 = int(txtNum2.get().strip())
            calculo.set(num1 + num2)
        else:
            calculo.set('Digite um número válido')

def subtracao():
    if verficaValores():
            num1 = int(txtNum1.get().strip())
            num2 = int(txtNum2.get().strip())
            calculo.set(num1 - num2)
    else:
        calculo.set('Digite um número válido')
        
def multiplicacao():
    if verficaValores():
            num1 = int(txtNum1.get().strip())
            num2 = int(txtNum2.get().strip())
            calculo.set(num1 * num2)
    else:
        calculo.set('Digite um número válido')

def divisao():
    if verficaValores():
            num1 = int(txtNum1.get().strip())
            num2 = int(txtNum2.get().strip())
            if(num2 == 0):
                calculo.set('Não pode ser dividido por 0, digite outro número.')
            else:
                calculo.set(num1 / num2)
    else:
        calculo.set('Digite um número válido')

def modulo():
    if verficaValores():
            num1 = int(txtNum1.get().strip())
            num2 = int(txtNum2.get().strip())
            if(num2 == 0):
                calculo.set('Não pode ser dividido por 0, digite outro número.')
            else:
                calculo.set(num1 % num2)
    else:
        calculo.set('Digite um número válido')

def fatorial():
    if len(txtNum1.get().strip()) < 1 or not txtNum1.get().strip().isnumeric():
        calculo.set('Digite um número válido')            
    else:
        num1 = int(txtNum1.get().strip())
        resul = num1
        for num in range(num1-1, 0, -1):
            resul *= num
        calculo.set(resul)  
            

# Instanciar tela
telaInicial = Tk()
telaInicial.geometry('850x600+800+200')

# Variavel Especial
calculo = StringVar()

#Cria e exibe o input
txtNum1 = Entry(telaInicial)
txtNum1.pack()

txtNum2 = Entry(telaInicial)
txtNum2.pack()

#Cria e exibe o botão
btnSomar = Button(
    telaInicial,
    text='Somar',
    command=somar
).pack()

btnSubtrair = Button(
    telaInicial,
    text='Subtração',
    command=subtracao
).pack()

btnMulti = Button(
    telaInicial,
    text='Multiplicação',
    command=multiplicacao
).pack()

btnDiv = Button(
    telaInicial,
    text='Divisão',
    command=divisao
).pack()

btnMod = Button(
    telaInicial,
    text='Modulo',
    command=modulo
).pack()

btnFat = Button(
    telaInicial,
    text='Fatorial',
    command=fatorial
).pack()


#Cria e exibe a etiqueta
lblResult = Label(
    telaInicial,
    #text = 'Resultado: ',
    font = 'Calibri 18', 
    #bg = '#cde',
    #fg = 'white',
    #bd = 3,
    #relief= 'solid',
    #padx = 10,
    #pady= 10,
    #width=50,
    #height=6,
    #anchor= W,  # N - top, S - Bottom, W - Left, E - Right (NW,NE, SW, SE), CENTER
    #justify=RIGHT
    textvariable=calculo,
)
calculo.set('Resultado: ')

lblResult.pack() # place / grid

lbltest = Label(telaInicial)
lbltest['text'] = 'Testando'
#lbltest.pack()

#print(lbltest.keys())
for item in lbltest.keys():
    print(f'{item} : {lbltest[item]}')    
    

#Exibe  a tela
telaInicial.mainloop()

