from Modelo.Figuras import Figura

class Retangulo(Figura):
    def desenhar(self, canvas):
        return canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.cor_borda, fill=self.cor_preenchimento)

    def to_dict(self):
        return {
            "tipo": "Retangulo",
            "x1": self.x1, "y1": self.y1,
            "x2": self.x2, "y2": self.y2,
            "cor_borda": self.cor_borda,
            "cor_preenchimento": self.cor_preenchimento
        }

    @staticmethod
    def from_dict(data):
        return Retangulo(
            data["x1"], data["y1"], data["x2"], data["y2"], 
            cor_borda=data["cor_borda"], cor_preenchimento=data["cor_preenchimento"]
        )
