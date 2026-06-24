import tkinter as tk

def seleciona_linha():
    global ferramenta
    ferramenta = "linha"

def seleciona_retangulo():
    global ferramenta
    ferramenta = "retangulo"

def seleciona_oval():
    global ferramenta
    ferramenta = "oval"

def marca_inicio(event):
    global ini_x, ini_y
    ini_x = event.x
    ini_y = event.y

def atualiza_figura(event):
    global figura_temp
    canvas.delete("preview")
    
    if ferramenta == "linha":
        canvas.create_line(ini_x, ini_y, event.x, event.y, tags = "preview")
    elif ferramenta == "retangulo":
        canvas.create_rectangle(ini_x, ini_y, event.x, event.y, tags = "preview")
    elif ferramenta == "oval":
        canvas.create_oval(ini_x, ini_y, event.x, event.y, tags = "preview")

def atualiza_fim(event):
   canvas.delete("preview")

   if ferramenta == "linha":
       canvas.create_line(ini_x, ini_y, event.x, event.y)
   elif ferramenta == "retangulo":
       canvas.create_rectangle(ini_x, ini_y, event.x, event.y)
   elif ferramenta == "oval":
       canvas.create_oval(ini_x, ini_y, event.x, event.y)

root = tk.Tk()

ferramenta = "linha"

frame = tk.Frame(root)
frame.pack()

tk.Button(frame, text = "Linha", command = seleciona_linha).pack(side = tk.LEFT)
tk.Button(frame, text = "Retângulo", command = seleciona_retangulo).pack(side = tk.LEFT)
tk.Button(frame, text = "Oval", command = seleciona_oval).pack(side = tk.LEFT)

canvas = tk.Canvas(root, bg='white', width=600, height=600)
canvas.pack()

canvas.bind("<ButtonPress-1>", marca_inicio)
canvas.bind("<B1-Motion>", atualiza_figura)
canvas.bind("<ButtonRelease-1>", atualiza_fim)

root.mainloop()