from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, x1, y1, x2, y2, cor_borda="black", cor_preenchimento=""):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    @abstractmethod
    def desenhar(self, canvas):
        raise NotImplementedError

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def from_dict(data):
        raise NotImplementedError

    def mover(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def contem(self, x, y):
        margem = 5
        return (min(self.x1, self.x2) - margem <= x <= max(self.x1, self.x2) + margem and
            min(self.y1, self.y2) - margem <= y <= max(self.y1, self.y2) + margem)