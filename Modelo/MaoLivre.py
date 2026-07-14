from Modelo.Figuras import Figura

class MaoLivre(Figura):
    def __init__(self, x1, y1, cor_borda="black"):
        super().__init__(x1, y1, x1, y1, cor_borda=cor_borda)
        self.pontos = [x1, y1]  

    def adicionar_ponto(self, x, y):
        self.pontos.extend([x, y]) 

    def desenhar(self, canvas, tags=None):
        if len(self.pontos) >= 4:  
            return canvas.create_line(self.pontos, fill=self.cor_borda, tags=tags)

    def to_dict(self):
        return {
            "tipo": "MaoLivre",
            "cor_borda": self.cor_borda,
            "pontos": self.pontos
        }

    @staticmethod
    def from_dict(data):
        # Cria uma instância básica temporária
        obj = MaoLivre(0, 0, cor_borda=data["cor_borda"])
        # Restaura a lista completa de pontos
        obj.pontos = data["pontos"]
        # Atualiza as coordenadas x1, y1, x2, y2 com os limites dos pontos restaurados
        if len(obj.pontos) >= 2:
            obj.x1, obj.y1 = obj.pontos[0], obj.pontos[1]
            obj.x2, obj.y2 = obj.pontos[-2], obj.pontos[-1]
        return obj
