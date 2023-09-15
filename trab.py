import tkinter as tk
from tkinter import messagebox
from tkinter import *

def continuar_enviar():
    nome = entrada_nome.get()
    mensagem = entrada_mensagem.get()

    if nome and mensagem:
        mensagem_janela = tk.Toplevel(janela_main)
        mensagem_janela.title("nome")

        mensagem_label = tk.Label(mensagem_janela, text=f"{nome} diz: {mensagem}")

        mensagem_label.pack()

    else:
        messagebox.showerror("deu ruim, coloque novamente", "Por Favor, insira um nome e uma mensagem")

janela_main = tk.Tk()
janela_main.title("mensagem")
janela_main.geometry('500x500')

info_nome = tk.Label(janela_main, text="Nome")
info_nome.pack()

entrada_nome = tk.Entry(janela_main)
entrada_nome.pack()

info_mensagem = tk.Label(janela_main, text="mensagem")
info_mensagem.pack()
entrada_mensagem = tk.Entry(janela_main)
entrada_mensagem.pack()

botao = tk.Button(janela_main, text="enviar", command=continuar_enviar)
botao.pack()

mensagem_esperando = tk.Label(janela_main,text ="esperando a mensagem do usuario")
mensagem_esperando.pack()
janela_main.mainloop()

