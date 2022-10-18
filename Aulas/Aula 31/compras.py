from tkinter import *
from tkinter import messagebox


# Funções
def limparCampo():
    txtItem.delete(0, END)
    txtItem.focus()

def verificarEntry():
    if len(txtItem.get().strip()) > 0:
        return True
    False

def adicionar():
    if verificarEntry():
        lista.insert(END, txtItem.get().strip())
        itens.append(txtItem.get().strip())
    limparCampo()
    print(itens)

def remover():
    indice = retornarIndex()
    if not indice == None:
        lista.delete(indice)
        del itens[indice]
    print(itens)

def retornarIndex():
    for indice in lista.curselection():
        return indice

def salvar():
    with open(f'{caminho}/listaDeCompras.txt', 'w', encoding="utf-8") as arquivo:
        for i in itens:
            arquivo.write(i + '\n')
    messagebox.showinfo(message='Lista Salva com Sucesso!')

def carregarArquivo():
    with open(f'{caminho}/listaDeCompras.txt', 'r', encoding="utf-8") as arq:
        for linha in arq:
            itens.append(str(linha).replace('\n',''))
            lista.insert(END, linha)
    print(itens)

# Variaveis
itens = []
caminho = './aulas/aula31'

run = Tk()
run.geometry('300x400+1280+200')
run.title('Lista de Compras')
run.resizable(False, False)

Label(run, text="Lista de Compras", font='Calibri 24').pack()

txtItem = Entry(run)
txtItem.pack()

Button(run, text='ADICIONAR', font='Arial 14', command=adicionar).pack()

lista = Listbox(run)
Label(run, font='Calibri 10').pack()
lista.pack()

Button(run, text='DELETAR', font='Arial 14', command=remover).pack()
Button(run, text='SALVAR', font='Arial 14', command=salvar).pack()

carregarArquivo()
run.mainloop()


''' 
    1 - Lista de telefones 
    2 - Nomes
    3 - Histórico de Calculadora
'''