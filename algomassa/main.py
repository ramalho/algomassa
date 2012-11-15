#!/usr/bin/env python3

import tkinter
from tkinter import ttk

LADO = 125
COLUNAS = 7
LINHAS = 6

root = tkinter.Tk()

QUADRADO = tkinter.PhotoImage(file='img/square125x.gif')
SETA = tkinter.PhotoImage(file='img/turtle125x.gif')
META = tkinter.PhotoImage(file='img/x125x.gif')

janela = tkinter.Frame(root, background='black')
janela['width'] = LADO * COLUNAS
janela['height'] = LADO * LINHAS

janela.grid()

def teclada(event):
    print(event)

casas = [[ttk.Label(janela, background='black', borderwidth=0) for i in range(COLUNAS)] for j in range(LINHAS)]
for j in range(LINHAS):
    for i, casa in enumerate(casas[j]):
        casa['image'] = QUADRADO
        casa.grid(row=j, column=i)
        casa.bind('<Key>', teclada)

janela.bind('<Key>', teclada)

root.mainloop()
