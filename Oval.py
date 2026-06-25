class Oval(Figura):
    def desenhar(self, canvas):
        return canvas.create_oval(self.x1, self.y1, self.x2, self.y2, outline = self.cor_borda, fill = self.cor_preenchimento)
