import tkinter as tk

class PaintView:
    def __init__(self, root, controller):  
        self.root = root
        self.controller = controller
        self.root.title("Paint Orientado a Objetos - MVC")
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()

        tk.Button(self.frame, text="Linha", command=lambda: self.controller.set_ferramenta("linha")).pack(side=tk.LEFT)
        tk.Button(self.frame, text="Retângulo", command=lambda: self.controller.set_ferramenta("retangulo")).pack(side=tk.LEFT)
        tk.Button(self.frame, text="Oval", command=lambda: self.controller.set_ferramenta("oval")).pack(side=tk.LEFT)
        tk.Button(self.frame, text="Mão Livre", command=lambda: self.controller.set_ferramenta("mao_livre")).pack(side=tk.LEFT)
        tk.Button(self.frame, text="Cor da Borda", command=self.controller.escolher_cor_borda).pack(side=tk.LEFT)
        tk.Button(self.frame, text="Preenchimento", command=self.controller.escolher_cor_preenchimento).pack(side=tk.LEFT)
        
        self.canvas = tk.Canvas(self.root, bg='white', width=600, height=600)
        self.canvas.pack()
        
        self.canvas.bind("<ButtonPress-1>", self.controller.marca_inicio)
        self.canvas.bind("<B1-Motion>", self.controller.update_figura)
        self.canvas.bind("<ButtonRelease-1>", self.controller.atualiza_fim)
