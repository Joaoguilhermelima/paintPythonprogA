
from Modelo.Linha import Linha
from Modelo.Retangulo import Retangulo
from Modelo.Oval import Oval
from Modelo.MaoLivre import MaoLivre

class EstadoFerramenta(ABC):
    @abstractmethod
    def pressionar(self, app, event): pass
    @abstractmethod
    def arrastar(self, app, event): pass
    @abstractmethod
    def soltar(self, app, event): pass

class EstadoLinha(EstadoFerramenta):
    def pressionar(self, app, event):
        app.ini_x, app.ini_y = event.x, event.y

    def arrastar(self, app, event):
        app.visualizador.canvas.delete("preview")
        app.visualizador.canvas.create_line(
            app.ini_x, app.ini_y, event.x, event.y, 
            fill=app.cor_borda, tags="preview"
        )

    def soltar(self, app, event):
        app.visualizador.canvas.delete("preview")
        figura = Linha(app.ini_x, app.ini_y, event.x, event.y, app.cor_borda)
        app.adicionar_figura(figura)


class EstadoRetangulo(EstadoFerramenta):
    def pressionar(self, app, event):
        app.ini_x, app.ini_y = event.x, event.y

    def arrastar(self, app, event):
        app.visualizador.canvas.delete("preview")
        app.visualizador.canvas.create_rectangle(
            app.ini_x, app.ini_y, event.x, event.y, 
            outline=app.cor_borda, fill=app.cor_preenchimento, tags="preview"
        )

    def soltar(self, app, event):
        app.visualizador.canvas.delete("preview")
        figura = Retangulo(app.ini_x, app.ini_y, event.x, event.y, app.cor_borda, app.cor_preenchimento)
        app.adicionar_figura(figura)


class EstadoOval(EstadoFerramenta):
    def pressionar(self, app, event):
        app.ini_x, app.ini_y = event.x, event.y

    def arrastar(self, app, event):
        app.visualizador.canvas.delete("preview")
        app.visualizador.canvas.create_oval(
            app.ini_x, app.ini_y, event.x, event.y, 
            outline=app.cor_borda, fill=app.cor_preenchimento, tags="preview"
        )

    def soltar(self, app, event):
        app.visualizador.canvas.delete("preview")
        figura = Oval(app.ini_x, app.ini_y, event.x, event.y, app.cor_borda, app.cor_preenchimento)
        app.adicionar_figura(figura)


class EstadoMaoLivre(EstadoFerramenta):
    def pressionar(self, app, event):
        app.mao_livre_ativa = MaoLivre(event.x, event.y, app.cor_borda)

    def arrastar(self, app, event):
        app.visualizador.canvas.delete("preview")
        if app.mao_livre_ativa:
            app.mao_livre_ativa.adicionar_ponto(event.x, event.y)
            app.mao_livre_ativa.desenhar(app.visualizador.canvas, tags="preview")

    def soltar(self, app, event):
        app.visualizador.canvas.delete("preview")
        if app.mao_livre_ativa:
            app.mao_livre_ativa.adicionar_ponto(event.x, event.y)
            app.adicionar_figura(app.mao_livre_ativa)
            app.mao_livre_ativa = None
