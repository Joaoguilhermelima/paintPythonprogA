from Figuras import Figura

class MaoLivre(Figura):
    def __init__(self, x1, y1, cor_borda="black"):
        super().__init__(x1, y1, x1, y1, cor_borda=cor_borda)
        self.pontos = [x1, y1]  

    def adicionar_ponto(self, x, y):
        self.pontos.extend([x, y]) 

    def desenhar(self, canvas, tags=None):
        if len(self.pontos) >= 4:  
            return canvas.create_line(self.pontos, fill=self.cor_borda, tags=tags)
