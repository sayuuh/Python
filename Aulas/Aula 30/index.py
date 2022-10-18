from random import choice
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

tela = Tk()
tela.geometry('300x500+1200+100')
tela.resizable(False, False)

# Checkbox = Caixa de seleção 
def salvar():
    print('Senha:', valorCheckbox.get())
valorCheckbox = IntVar()
checkSalvar = Checkbutton(tela, text='Deseja salvar a senha?', variable=valorCheckbox, command=salvar)
checkSalvar.select()
checkSalvar.pack()

# Radiobutton 
valorRadio = IntVar()
valorRadio2 = IntVar()
def radio():
    radio2.config(state=DISABLED)
    radio3.config(state=DISABLED)
    radio4.config(state=DISABLED)
    box.config(state=DISABLED)
    checkSalvar.config(state=DISABLED)
    listaDeAlunos.config(state=DISABLED)
    slide.config(state=ACTIVE)

radio1 = Radiobutton(tela, text='1 Quarto', variable=valorRadio, value=1, command=radio)
radio2 = Radiobutton(tela, text='2 Quartos', variable=valorRadio, value=2)
radio3 = Radiobutton(tela, text='3 Quartos', variable=valorRadio, value=3)
radio4 = Radiobutton(tela, text='4 Quartos', variable=valorRadio, value=4)
radio3.select()
radio2.focus()
radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()

radioA = Radiobutton(tela, text='Rio de Janeiro', variable=valorRadio2, value=1)
radioB= Radiobutton(tela, text='São Paulo', variable=valorRadio2, value=2)
radioC = Radiobutton(tela, text='Minas Gerais', variable=valorRadio2, value=3)
radioC.select()
radioA.pack()
radioB.pack()
radioC.pack()

# Escala 
def verValor(valor):
    print(valor)
slide = Scale(tela, from_=0.5, to=90.5, orient=HORIZONTAL, resolution=0.2, command=verValor)
slide.pack()

# ComboBox
alunos = ['Selecione o Aluno','Aba', 'Akio', 'Kenji', 'Mateus', 'Sayumi', 'Erick', 'Davi']
box = Combobox(tela, values=alunos)
box.set(choice(alunos))
box.pack()

# Listas
listaDeAlunos = Listbox(tela)
#listaDeAlunos.insert(END, 'Valor 0')
for aluno in alunos:
    listaDeAlunos.insert(END, aluno)
listaDeAlunos.pack()
#  Retorna index do item selecionado
def retornaIndexSelecionadoNaLista():
    for index in listaDeAlunos.curselection():
        return index

# Button
def ver():
    print('Resultados')
    print('Checkbox:', valorCheckbox.get())
    print('Radio:', valorRadio.get())
    print('Slide:', slide.get())
    if box.current() == 0:
        messagebox.showwarning(message='Selecione um aluno')
    else:
        print('Combo: ', box.get())
    print('Lista: ', listaDeAlunos.get(ACTIVE))
    print('Lista selecionado: ')
    listaDeAlunos.delete(retornaIndexSelecionadoNaLista())
    listaDeAlunos.insert(END, 'Outro Aluno')
Button(tela, text='Ver', command=ver).pack()
tela.mainloop()