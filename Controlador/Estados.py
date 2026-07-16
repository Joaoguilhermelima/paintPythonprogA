class EstadoSelecao(EstadoFerramenta):
    def pressionar(self, app, event):
        adicionar = (event.state & 0x0001) != 0  # Verifica se a tecla Shift está pressionada

        app.selecionar_figura(event.x, event.y, adicionar)
        # Verifica se o Shift foi pressionado durante o clique
        acumular = bool(event.state & 0x0001)  # 0x0001 representa o estado da tecla Shift no Tkinter
        app.selecionar_figura(event.x, event.y, acumular=acumular)
        app.ultimo_x = event.x
        app.ultimo_y = event.y

    def arrastar(self, app, event):
        if app.figuras_selecionadas is None:
        if not app.figuras_selecionadas:
            return

        dx = event.x - app.ultimo_x
        dy = event.y - app.ultimo_y

        for figura in app.figuras_selecionadas:
            figura.mover(dx, dy)
        # Move todos os elementos selecionados simultaneamente (inclusive Grupos)
        for fig in app.figuras_selecionadas:
            fig.mover(dx, dy)

        app.ultimo_x = event.x
        app.ultimo_y = event.y
        app.atualizar_visualizador()

    def soltar(self, app, event):
        pass

    def apagar_selecionadas(self):
        for figura in self.figuras_selecionadas:
            if figura in self.figuras:
                self.figuras.remove(figura)

        self.figuras_selecionadas.clear()
        self.atualizar_visualizador()
