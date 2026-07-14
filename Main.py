import tkinter as tk
from tkinter import colorchooser
# Importamos o controlador que gerencia toda a lógica
from Controlador.ControladorDesenho import ControladorDesenho 
from Controlador.Estados import EstadoLinha, EstadoRetangulo, EstadoOval, EstadoMaoLivre

# Agora não precisamos de funções soltas e variáveis globais!
root = tk.Tk()
root.title("Editor de Desenho")

# Criamos a tela normalmente
canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()

# Criamos o Controlador e passamos o "visualizador" (a própria janela/canvas) para ele
# O controlador vai gerenciar as figuras e os estados de desenho
class VisualizadorMock:
    def __init__(self, canvas):
        self.canvas = canvas

visualizador = VisualizadorMock(canvas)
controlador = ControladorDesenho(visualizador)

# Funções auxiliares simplificadas para os botões acionarem o controlador:
def mudar_para_linha():
    controlador.definir_estado(EstadoLinha())

def mudar_para_retangulo():
    controlador.definir_estado(EstadoRetangulo())

def mudar_para_oval():
    controlador.definir_estado(EstadoOval())

def mudar_para_maolivre():
    controlador.definir_estado(EstadoMaoLivre())

# --- MENU E BOTÕES ---
frame = tk.Frame(root)
frame.pack()

# Botões de ferramentas
tk.Button(frame, text="Linha", command=mudar_para_linha).pack(side=tk.LEFT)
tk.Button(frame, text="Retângulo", command=mudar_para_retangulo).pack(side=tk.LEFT)
tk.Button(frame, text="Oval", command=mudar_para_oval).pack(side=tk.LEFT)
tk.Button(frame, text="Mão Livre", command=mudar_para_maolivre).pack(side=tk.LEFT)

# Botões de configuração (chamam métodos do controlador)
tk.Button(frame, text="Cor Borda", command=controlador.escolhe_cor_borda).pack(side=tk.LEFT)
tk.Button(frame, text="Cor Preenchimento", command=controlador.escolhe_cor_preenchimento).pack(side=tk.LEFT)

# OS NOVOS BOTÕES: Apenas chamam as funções do controlador!
tk.Button(frame, text="Salvar", command=controlador.salvar).pack(side=tk.LEFT)
tk.Button(frame, text="Abrir", command=controlador.abrir).pack(side=tk.LEFT)

# Os eventos do mouse são repassados para o controlador gerenciar através do estado ativo
canvas.bind("<ButtonPress-1>", lambda event: controlador.estado_atual.pressionar(event, controlador))
canvas.bind("<B1-Motion>", lambda event: controlador.estado_atual.arrastar(event, controlador))
canvas.bind("<ButtonRelease-1>", lambda event: controlador.estado_atual.soltar(event, controlador))

root.mainloop()
