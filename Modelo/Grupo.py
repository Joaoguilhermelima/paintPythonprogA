from Modelo.Figuras import Figura

class Grupo(Figura):
    def __init__(self, figuras=None, cor_borda="black", cor_preenchimento=""):
        super().__init__(0, 0, 0, 0, cor_borda=cor_borda, cor_preenchimento=cor_preenchimento)
        self.figuras = figuras if figuras is not None else []
        self.recalcular_limites()

    def recalcular_limites(self):             #Calcula a área mínima necessária para englobar todas as figuras do grupo
        if not self.figuras:
            self.x1, self.y1, self.x2, self.y2 = 0, 0, 0, 0
            return

        x1_list, y1_list, x2_list, y2_list = [], [], [], []
        for fig in self.figuras:
            x1_list.append(min(fig.x1, fig.x2))
            y1_list.append(min(fig.y1, fig.y2))
            x2_list.append(max(fig.x1, fig.x2))
            y2_list.append(max(fig.y1, fig.y2))

        self.x1 = min(x1_list)
        self.y1 = min(y1_list)
        self.x2 = max(x2_list)
        self.y2 = max(y2_list)

    def desenhar(self, canvas):    # Percorre a lista de figuras internas e desenha cada uma delas na tela
        for fig in self.figuras:
            fig.desenhar(canvas)

    def mover(self, dx, dy):     # Desloca todas as figuras internas e a própria caixa limite do grupo pelas distâncias especificadas
        for fig in self.figuras:
            fig.mover(dx, dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def contem(self, x, y):   # Desloca todas as figuras internas e a própria caixa limite do grupo pelas distâncias especificadas
        for fig in self.figuras:
            if fig.contem(x, y):
                return True
        return False

    @property
    def cor_borda(self):     # Altera a cor de contorno do grupo e propaga essa nova cor para todas as figuras internas
        return self._cor_borda

    @cor_borda.setter
    def cor_borda(self, cor):
        self._cor_borda = cor
        for fig in self.figuras:
            fig.cor_borda = cor

    @property
    def cor_preenchimento(self):   # Altera a cor de preenchimento do grupo e propaga essa nova cor para todas as figuras internas
        return self._cor_preenchimento

    @cor_preenchimento.setter
    def cor_preenchimento(self, cor):
        self._cor_preenchimento = cor
        for fig in self.figuras:
            fig.cor_preenchimento = cor

    def to_dict(self):             # Transforma o grupo e suas subfiguras em um dicionário para permitir que o desenho seja salvo em arquivo
        return { 
            "tipo": "Grupo",
            "figuras": [fig.to_dict() for fig in self.figuras],
            "cor_borda": self.cor_borda,
            "cor_preenchimento": self.cor_preenchimento
        }

    @staticmethod
    def from_dict(data):          # Lê o dicionário salvo, identifica os tipos de figuras e reconstrói o objeto Grupo original
        from Modelo.Linha import Linha
        from Modelo.Retangulo import Retangulo
        from Modelo.Oval import Oval
        from Modelo.MaoLivre import MaoLivre
        
        mapeamento = {
            "Linha": Linha,
            "Retangulo": Retangulo,
            "Oval": Oval,
            "MaoLivre": MaoLivre,
            "Grupo": Grupo
        }
        
        figuras_reconstruidas = []
        for item in data["figuras"]:
            tipo = item.get("tipo")
            if tipo in mapeamento:
                figuras_reconstruidas.append(mapeamento[tipo].from_dict(item))
                
        grupo = Grupo(figuras_reconstruidas, cor_borda=data["cor_borda"], cor_preenchimento=data["cor_preenchimento"])
        return grupo
