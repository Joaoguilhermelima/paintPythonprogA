
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import tkinter as tk
from tkinter import colorchooser
from Controlador.Codigo import ControladorDesenho
from Controlador.Estados import EstadoLinha, EstadoRetangulo, EstadoOval, EstadoMaoLi

from Controlador.Codigo import ControladorDesenho 
from Controlador.Estados import EstadoLinha, EstadoRetangulo, EstadoOval, EstadoMaoLivre

root = tk.Tk()
root.title("Editor de Desenho")

canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()


class VisualizadorMock:
    def __init__(self, canvas):
        self.canvas = canvas

visualizador = VisualizadorMock(canvas)
controlador = ControladorDesenho(visualizador)


def mudar_para_linha():
    controlador.definir_estado(EstadoLinha())

def mudar_para_retangulo():
    controlador.definir_estado(EstadoRetangulo())

def mudar_para_oval():
    controlador.definir_estado(EstadoOval())

def mudar_para_maolivre():
    controlador.definir_estado(EstadoMaoLivre())


frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Linha", command=mudar_para_linha).pack(side=tk.LEFT)
tk.Button(frame, text="Retângulo", command=mudar_para_retangulo).pack(side=tk.LEFT)
tk.Button(frame, text="Oval", command=mudar_para_oval).pack(side=tk.LEFT)
tk.Button(frame, text="Mão Livre", command=mudar_para_maolivre).pack(side=tk.LEFT)

tk.Button(frame, text="Cor Borda", command=controlador.escolhe_cor_borda).pack(side=tk.LEFT)
tk.Button(frame, text="Cor Preenchimento", command=controlador.escolhe_cor_preenchimento).pack(side=tk.LEFT)

tk.Button(frame, text="Salvar", command=controlador.salvar).pack(side=tk.LEFT)
tk.Button(frame, text="Abrir", command=controlador.abrir).pack(side=tk.LEFT)


canvas.bind("<ButtonPress-1>", lambda event: controlador.estado_atual.pressionar(controlador, event))
canvas.bind("<B1-Motion>", lambda event: controlador.estado_atual.arrastar(controlador, event))
canvas.bind("<ButtonRelease-1>", lambda event: controlador.estado_atual.soltar(controlador, event))

root.mainloop()
