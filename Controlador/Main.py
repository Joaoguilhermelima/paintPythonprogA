import sys
import os
import tkinter as tk

raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if raiz not in sys.path:
    sys.path.insert(0, raiz)

from Controlador.Codigo import ControladorDesenho
from Controlador.Estados import EstadoLinha, EstadoRetangulo, EstadoOval, EstadoMaoLivre, EstadoSelecao

root = tk.Tk()
root.title("Editor de Desenho Vetorial - Composite")

canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()

class VisualizadorMock:
    def __init__(self, canvas):
        self.canvas = canvas

visualizador = VisualizadorMock(canvas)
controlador = ControladorDesenho(visualizador)

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text="Linha", command=lambda: controlador.definir_estado(EstadoLinha())).pack(side=tk.LEFT)
tk.Button(frame, text="Retângulo", command=lambda: controlador.definir_estado(EstadoRetangulo())).pack(side=tk.LEFT)
tk.Button(frame, text="Oval", command=lambda: controlador.definir_estado(EstadoOval())).pack(side=tk.LEFT)
tk.Button(frame, text="Mão Livre", command=lambda: controlador.definir_estado(EstadoMaoLivre())).pack(side=tk.LEFT)
tk.Button(frame, text="Selecionar", command=lambda: controlador.definir_estado(EstadoSelecao())).pack(side=tk.LEFT)

tk.Button(frame, text="Agrupar", command=controlador.agrupar).pack(side=tk.LEFT)
tk.Button(frame, text="Desagrupar", command=controlador.desagrupar).pack(side=tk.LEFT)

tk.Button(frame, text="Cor Borda", command=controlador.escolhe_cor_borda).pack(side=tk.LEFT)
tk.Button(frame, text="Cor Preenchimento", command=controlador.escolhe_cor_preenchimento).pack(side=tk.LEFT)
tk.Button(frame, text="Salvar", command=controlador.salvar).pack(side=tk.LEFT)
tk.Button(frame, text="Abrir", command=controlador.abrir).pack(side=tk.LEFT)


canvas.bind("<ButtonPress-1>", lambda event: controlador.estado_atual.pressionar(controlador, event))
canvas.bind("<B1-Motion>", lambda event: controlador.estado_atual.arrastar(controlador, event))
canvas.bind("<ButtonRelease-1>", lambda event: controlador.estado_atual.soltar(controlador, event))
root.bind("<Delete>", lambda event: controlador.apagar_selecionada())

root.mainloop()
