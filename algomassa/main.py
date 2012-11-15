#!/usr/bin/env python3

import tkinter
from tkinter import ttk
from random import randrange

LADO = 125
COLUNAS = 7
LINHAS = 6

root = tkinter.Tk()

QUADRADO = tkinter.PhotoImage(file='img/square125x.gif')
TARTARUGAS = [tkinter.PhotoImage(file='img/turtle125x-r%03d.gif' % rot)
         for rot in range(0, 360, 45)]
META = tkinter.PhotoImage(file='img/x125x.gif')

MOVIMENTOS = {
    'n' : (0, -1),
    'e' : (1, 0),
    's' : (0, 1),
    'w' : (-1, 0)
}

janela = tkinter.Frame(root, background='black', borderwidth=0)
janela['width'] = LADO * COLUNAS
janela['height'] = LADO * LINHAS

janela.grid()

class Tabuleiro(tkinter.Canvas):
    def __init__(self, parent, *kwargs):
        super(Tabuleiro, self).__init__(parent, *kwargs)
        self.configure(background='black', width=LADO*COLUNAS, height=LADO*LINHAS, borderwidth=0)
        self.casas = [[self.create_image((i*LADO, j*LADO), image=QUADRADO, anchor='nw')
                          for i in range(COLUNAS)]
                      for j in range(LINHAS)]
        self.tartaruga = Tartaruga(self, 3, 5)
        parent.bind('<Right>', self.tartaruga.direita)
        parent.bind('<Up>', self.tartaruga.frente)
        self.meta = (randrange(COLUNAS)//2*2, randrange(LINHAS//2))
        print(self.meta)
        self.meta_figura = self.create_image(self.meta[0]*LADO, self.meta[1]*LADO, image=META, anchor='nw')

class Tartaruga(object):
    def __init__(self, tabuleiro, coluna, linha, direcao='n'):
        self.tabuleiro = tabuleiro
        self.coluna = coluna
        self.linha = linha
        self.direcao = direcao
        self.desenhar('nesw'.index(self.direcao))

    def desenhar(self, indice_fig):
        pos = (self.coluna*LADO, self.linha*LADO)
        figura_antiga = getattr(self, 'figura', None)
        self.figura = self.tabuleiro.create_image(pos,
            image=TARTARUGAS[indice_fig], anchor='nw')
        if figura_antiga:
            tabuleiro.delete(figura_antiga)

    def direita(self, evento):
        indice = ('nesw'.index(self.direcao) + 1) % 4
        self.direcao = 'nesw'[indice]
        self.desenhar(indice*2-1)
        self.tabuleiro.after(75, self.direita_completar)

    def direita_completar(self):
        indice = 'nesw'.index(self.direcao)
        self.desenhar(indice*2)

    def frente(self, evento):
        dj, di = MOVIMENTOS[self.direcao]
        self.coluna = (self.coluna + dj/2) % COLUNAS
        self.linha = (self.linha + di/2) % LINHAS
        self.desenhar('nesw'.index(self.direcao)*2)
        self.tabuleiro.after(75, self.frente_completar)

    def frente_completar(self):
        dj, di = MOVIMENTOS[self.direcao]
        self.coluna = (self.coluna + dj/2) % COLUNAS
        self.linha = (self.linha + di/2) % LINHAS
        self.desenhar('nesw'.index(self.direcao)*2)

tabuleiro = Tabuleiro(janela)
tabuleiro.grid()

janela.focus_set()

root.mainloop()
