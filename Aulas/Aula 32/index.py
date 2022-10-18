from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

def info(msg):
    messagebox.showinfo(title='Mensagem', message=msg)   
    
def limparCampo():
    txtNome.delete(0, END)
    txtTelefone.delete(0, END)
    txtNome.focus()

def inserir():
    if len(txtNome.get().strip()) < 1 or len(txtTelefone.get().strip()) < 1:
        info('Preencha os campos corretamente.')
    else:
        tabela.insert('', END, values=(9876, txtNome.get().strip().upper(), txtTelefone.get().strip()))
        salvar()
    limparCampo()

def ver():
    itemSelecionado = tabela.selection()[0]
    if not len(itemSelecionado) == 0:
        limparCampo()
        txtNome.insert(0, tabela.item(itemSelecionado, 'values')[1])
        txtTelefone.insert(0, tabela.item(itemSelecionado, 'values')[2])
    else:
        info('Selecione um item')

def deletar():
    itemSelecionado = tabela.selection()
    print(itemSelecionado)
    if not len(itemSelecionado) == 0:
        for i in itemSelecionado:
            tabela.delete(i)
        salvar()
    else:
        info('Selecione um item da lista.')

def salvar():
    print(tabela.get_children())
    with open(f'{caminho}/agenda.txt', 'w') as arquivo:
        for i in tabela.get_children():
            #(codigo;nome;telefone)
            #(codigo;nome;telefone)
            variavel = f"{tabela.item(i, 'values')[0]};{tabela.item(i, 'values')[1]};{tabela.item(i, 'values')[2]}\n"
            arquivo.write(variavel)

def carregar():
    with open(f'{caminho}/agenda.txt', 'r') as arquivo:
        for linha in arquivo:
            valores = linha.split(';')
            tabela.insert('', END, values=(valores[0], valores[1], valores[2].replace('\n', '')))

caminho = './aulas/aula32'

run = Tk()
run.title('Agenda')
run.geometry('+1200+120')

lista = [[1234, 'Nome Nome', '210988796324'],[4321, 'Sobrenome Sobrenome', '1165487796324'], [7894, 'Ultimonome Ultimonome', '3242165496324'], [9194, 'Semnome Semnome', '0978946321']]

Label(run, text='Nome').grid(row=0, column=0)
Label(run, text='Telefone').grid(row=0, column=1)

txtNome = Entry(run)
txtNome.grid(row=1, column=0)

txtTelefone = Entry(run)
txtTelefone.grid(row=1, column=1)


tabela = Treeview(run, columns=(0, 1, 2), show='headings') #columns=('id','nome','telefone') selectmode='browse'

tabela.column(0, minwidth=40, width=50)
tabela.column(1, minwidth=150, width=350)
tabela.column(2, minwidth=80, width=150)

tabela.heading(0, text='ID')
tabela.heading(1, text='NOME')
tabela.heading(2, text='TELEFONE')



tabela.grid(row=4, columnspan=3, pady=10, padx=10) #place(x=10, y=10, width=500, height=300) #pack(padx=10, pady=10)

Button(run, text='Inserir', command=inserir).grid(row=5, column=0, pady=10)
Button(run, text='Ver', command=ver).grid(row=5, column=1, pady=10)
Button(run, text='Deletar', command=deletar).grid(row=5, column=2, pady=10)

#for itens in lista:
    #tabela.insert('', END, values=(itens[0], itens[1].upper(), itens[2]))
carregar()

run.mainloop()


''' 
    CASA 
    1 - Janela
        - Lista de Produtos (NOME, VALOR)
        - Entry quantidade
        - Button Inserir
        - Label (total = qnt x valor)
        - Tabela (Nome Produto, Preco_Unit, Qnt, Total)
        - Label (Total da Compra)
        - Buttons
            - Finalizar Compra, Deletar
    
    JANELA
    COMBOBOX    QTN
    TOTAL       BTNINSERIR
            TABELA
    TOTAL DA COMPRA
        FINALIZAR COMPRA e DELETAR ITEM


'''