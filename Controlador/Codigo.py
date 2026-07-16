import json
from tkinter import filedialog, colorchooser
from Controlador.Estados import EstadoLinha, EstadoRetangulo, EstadoOval, EstadoMaoLivre
from Modelo.Linha import Linha
from Modelo.Retangulo import Retangulo
from Modelo.Oval import Oval
from Modelo.MaoLivre import MaoLivre

class ControladorDesenho:
    def __init__(self, visualizador):
        self.visualizador = visualizador
        self.figuras = []
        self.estado_atual = EstadoLinha()

        self.cor_borda = "black"
        self.cor_preenchimento = ""

        self.ini_x = 0
        self.ini_y = 0
        self.mao_livre_ativa = None
        self.figura_selecionada = None

        self.ultimo_x = 0
        self.ultimo_y = 0



    def definir_estado(self, novo_estado):
        self.estado_atual = novo_estado

    def escolhe_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda")[1]
        if cor:
            if self.figura_selecionada:
                self.figura_selecionada.cor_borda = cor
                self.atualizar_visualizador()
            else:
                self.cor_borda = cor

    def escolhe_cor_preenchimento(self):
        cor = colorchooser.askcolor(title="Escolha a cor de preenchimento")[1]
        if cor:
            if self.figura_selecionada:
                self.figura_selecionada.cor_preenchimento = cor
                self.atualizar_visualizador()
            else:
                self.cor_preenchimento = cor

    def adicionar_figura(self, figura):
        self.figuras.append(figura)
        self.atualizar_visualizador()

    def atualizar_visualizador(self):
        self.visualizador.canvas.delete("all")
        for fig in self.figuras:
            fig.desenhar(self.visualizador.canvas)

    def salvar(self):
        caminho = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if caminho:
         
            dados = [fig.to_dict() for fig in self.figuras]
            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4)

    def abrir(self):
        caminho = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            mapeamento = {
                "Linha": Linha,
                "Retangulo": Retangulo,
                "Oval": Oval,
                "MaoLivre": MaoLivre
            }
            
            self.figuras = []
            for item in dados:
                tipo = item.get("tipo")
                if tipo in mapeamento:
                    
                    self.figuras.append(mapeamento[tipo].from_dict(item))
            
            self.atualizar_visualizador()

    def selecionar_figura(self, x, y):
        self.figura_selecionada = None

        for figura in reversed(self.figuras):
            if figura.contem(x, y):
                self.figura_selecionada = figura
                break

    def apagar_selecionada(self):
        if self.figura_selecionada:
            self.figuras.remove(self.figura_selecionada)
            self.figura_selecionada = None
            self.atualizar_visualizador()