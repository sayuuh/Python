from dis import show_code
from textwrap import shorten
from tkinter import *
from tkinter import messagebox

t1 = Tk()
t1.geometry('500x500+1200+100')

def limparCampo():
    txtNum1.delete(0, END)
    txtNum2.delete(0, END)
    txtNum1.focus()

def verificaValor():
    if len(txtNum1.get().strip()) < 1:
        messagebox.showwarning(title='Mensagem', message='Digite um número')
        return False
    if not txtNum1.get().strip().isnumeric():
        messagebox.showerror(title='Mensagem', message='Digite um número')
        return False
    if len(txtNum2.get().strip()) < 1:
        messagebox.showwarning(title='Mensagem', message='Digite um número')
        return False
    if not txtNum2.get().strip().isnumeric():
        messagebox.showerror(title='Mensagem', message='Digite um número')
        return False
    return True

def somar():
    # showerror, showwarning, showinfo
    # messagebox.showinfo(title='Alert', message='Efetuar SOMA')
    # messagebox.showwarning(title='Alert', message='Efetuar SOMA')
    # messagebox.showerror(title='Alert', message='Efetuar SOMA')
    if verificaValor():
        # messagebox.showinfo(title='Mensagem', message='Ok')
        soma = int(txtNum1.get()) + int(txtNum2.get())
        # print(txtPassword.get())
        lblResultado['text'] = f'{txtNum1.get()} + {txtNum2.get()} = {soma}'
        limparCampo()

def subtrair():
    if verificaValor():
        soma = int(txtNum1.get()) - int(txtNum2.get())
        lblResultado['text'] = f'{txtNum1.get()} - {txtNum2.get()} = {soma}'
        limparCampo()

def multiplicar():
    if verificaValor():
        soma = int(txtNum1.get()) * int(txtNum2.get())
        lblResultado['text'] = f'{txtNum1.get()} x {txtNum2.get()} = {soma}'
        limparCampo()

def dividir():
    if verificaValor():
        if int(txtNum2.get()) !=0:    
            soma = int(txtNum1.get()) / int(txtNum2.get())
            lblResultado['text'] = f'{txtNum1.get()} / {txtNum2.get()} = {soma}'
            limparCampo()
        else:
            messagebox.showerror(title='Mensagem', message='Não pode ser dividido por 0')
            limparCampo()

# ___________LAYOUT____________ #
txtNum1 = Entry(t1)
txtNum2 = Entry(t1)
# txtPassword = Entry(t1, show='*') # Campo de senha

btnSomar = Button(t1, text='Somar', command=somar)
btnSubtrair = Button(t1, text='Subtrair', command=subtrair)
btnMultiplicar = Button(t1, text='Multiplicar', command=multiplicar)
btnDividir = Button(t1, text='Dividir', command=dividir)

lblResultado = Label(t1)

# ___________EXIBIR____________ #
txtNum1.pack()
txtNum2.pack()

btnSomar.pack()
btnSubtrair.pack()
btnMultiplicar.pack()
btnDividir.pack()

lblResultado.pack()
# txtPassword.pack()



t1.mainloop()