import tkinter as tk
from tkinter import colorchooser
from MaoLivre import MaoLivre

def seleciona_maolivre():
    global ferramenta
    ferramenta = "maolivre"

def seleciona_linha():
    global ferramenta
    ferramenta = "linha"

def seleciona_retangulo():
    global ferramenta
    ferramenta = "retangulo"

def seleciona_oval():
    global ferramenta
    ferramenta = "oval"

def escolhe_cor_borda():
    global cor_borda
    cor = colorchooser.askcolor(title = "Escolha a cor da borda")[1]
    if cor:  
        cor_borda = cor

def escolhe_cor_preenchimento():
    global cor_preenchimento
    cor = colorchooser.askcolor(title = "Escolha a cor de preenchimento")[1]
    if cor:  
        cor_preenchimento = cor

def marca_inicio(event):
    global ini_x, ini_y, mao_livre
    ini_x = event.x
    ini_y = event.y

    if ferramenta == "maolivre":
        mao_livre = MaoLivre(event.x, event.y, cor_borda)

def atualiza_figura(event):
    global figura_temp, mao_livre

    if ferramenta == "maolivre":
        canvas.delete("preview")
        mao_livre.adicionar_ponto(event.x, event.y)
        mao_livre.desenhar(canvas, tags="preview")
        return
    
    canvas.delete("preview")
    
    if ferramenta == "linha":
        canvas.create_line(ini_x, ini_y, event.x, event.y, fill = cor_borda, tags = "preview")
    elif ferramenta == "retangulo":
        canvas.create_rectangle(ini_x, ini_y, event.x, event.y, outline = cor_borda, fill = cor_preenchimento, tags = "preview")
    elif ferramenta == "oval":
        canvas.create_oval(ini_x, ini_y, event.x, event.y, outline = cor_borda, fill = cor_preenchimento, tags = "preview")

def atualiza_fim(event):
   global mao_livre
   canvas.delete("preview")


   if ferramenta == "linha":
       canvas.create_line(ini_x, ini_y, event.x, event.y, fill = cor_borda)
   elif ferramenta == "retangulo":
       canvas.create_rectangle(ini_x, ini_y, event.x, event.y, outline = cor_borda, fill = cor_preenchimento)
   elif ferramenta == "oval":
       canvas.create_oval(ini_x, ini_y, event.x, event.y, outline = cor_borda, fill = cor_preenchimento)
   elif ferramenta == "maolivre":
       mao_livre.adicionar_ponto(event.x, event.y)
       mao_livre.desenhar(canvas)
       mao_livre = None

root = tk.Tk()

ferramenta = "linha"
cor_borda = "black"
cor_preenchimento = ""
mao_livre = None

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text = "Linha", command = seleciona_linha).pack(side = tk.LEFT)
tk.Button(frame, text = "Retângulo", command = seleciona_retangulo).pack(side = tk.LEFT)
tk.Button(frame, text = "Oval", command = seleciona_oval).pack(side = tk.LEFT)
tk.Button(frame, text="Mão Livre", command=seleciona_maolivre).pack(side=tk.LEFT)
tk.Button(frame, text = "Cor da borda", command = escolhe_cor_borda).pack(side = tk.LEFT)
tk.Button(frame, text = "Cor de preenchimento", command = escolhe_cor_preenchimento).pack(side = tk.LEFT)

canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()

canvas.bind("<ButtonPress-1>", marca_inicio)
canvas.bind("<B1-Motion>", atualiza_figura)
canvas.bind("<ButtonRelease-1>", atualiza_fim)

root.mainloop()
