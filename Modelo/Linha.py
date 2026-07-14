from Modelo.Figuras import Figura

class Linha(Figura):
    def desenhar(self, canvas):
        return canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.cor_borda)

    def to_dict(self):
        return {
            "tipo": "Linha",
            "x1": self.x1, "y1": self.y1,
            "x2": self.x2, "y2": self.y2,
            "cor_borda": self.cor_borda
        }

    @staticmethod
    def from_dict(data):
        return Linha(data["x1"], data["y1"], data["x2"], data["y2"], cor_borda=data["cor_borda"])
