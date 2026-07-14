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
