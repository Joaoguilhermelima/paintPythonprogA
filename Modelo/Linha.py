from Figuras import Figura

class Linha(Figura):
    def desenhar(self, canvas):
        return canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = self.cor_borda)
