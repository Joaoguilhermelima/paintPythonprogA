import json
from tkinter import filedialog, colorchooser
from Controlador.Estados import EstadoLinha, EstadoRetangulo, EstadoOval, EstadoMaoLivre
from Modelo.Linha import Linha
from Modelo.Retangulo import Retangulo
from Modelo.Oval import Oval
from Modelo.MaoLivre import MaoLivre
from Modelo.Grupo import Grupo

class ControladorDesenho:
    def __init__(self, visualizador):
        self.visualizador = visualizador
        self.figuras = []
        self.estado_atual = EstadoLinha()

        self.cor_borda = "black"
        self.cor_preenchimento = ""

        self.ini_x = 0
        self.ini_y = 0
        self.mao_livre_ativa = None
        
        # Agora gerenciamos uma lista de figuras selecionadas
        self.figuras_selecionadas = []
        self.ultimo_x = 0
        self.ultimo_y = 0

    @property
    def figura_selecionada(self):
        """Propriedade para compatibilidade legada: retorna a última selecionada."""
        return self.figuras_selecionadas[-1] if self.figuras_selecionadas else None

    def definir_estado(self, novo_estado):
        # Ao mudar de estado (ex: de Seleção para Linha), limpa as seleções
        self.figuras_selecionadas.clear()
        self.atualizar_visualizador()
        self.estado_atual = novo_estado

    def escolhe_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda")[1]
        if cor:
            if self.figuras_selecionadas:
                for fig in self.figuras_selecionadas:
                    fig.cor_borda = cor
                self.atualizar_visualizador()
            else:
                self.cor_borda = cor

    def escolhe_cor_preenchimento(self):
        cor = colorchooser.askcolor(title="Escolha a cor de preenchimento")[1]
        if cor:
            if self.figuras_selecionadas:
                for fig in self.figuras_selecionadas:
                    # Apenas altera se a figura possuir o atributo de preenchimento
                    if hasattr(fig, 'cor_preenchimento'):
                        fig.cor_preenchimento = cor
                self.atualizar_visualizador()
            else:
                self.cor_preenchimento = cor

    def adicionar_figura(self, figura):
        self.figuras.append(figura)
        self.atualizar_visualizador()

    def atualizar_visualizador(self):
        self.visualizador.canvas.delete("all")
        for fig in self.figuras:
            fig.desenhar(self.visualizador.canvas)
        
        # Destaca visualmente as figuras selecionadas com uma borda tracejada de auxílio
        for fig in self.figuras_selecionadas:
            margin = 3
            self.visualizador.canvas.create_rectangle(
                min(fig.x1, fig.x2) - margin, min(fig.y1, fig.y2) - margin,
                max(fig.x1, fig.x2) + margin, max(fig.y1, fig.y2) + margin,
                outline="blue", dash=(2, 2)
            )

    def selecionar_figura(self, x, y, acumular=False):
        """Seleciona figuras com suporte a seleção múltipla (usando Shift/acumular)."""
        if not acumular:
            self.figuras_selecionadas.clear()

        for figura in reversed(self.figuras):
            if figura.contem(x, y):
                if figura in self.figuras_selecionadas:
                    self.figuras_selecionadas.remove(figura) # Remove se clicar de novo
                else:
                    self.figuras_selecionadas.append(figura)
                break
        
        self.atualizar_visualizador()

    def apagar_selecionada(self):
        if self.figuras_selecionadas:
            for fig in self.figuras_selecionadas:
                if fig in self.figuras:
                    self.figuras.remove(fig)
            self.figuras_selecionadas.clear()
            self.atualizar_visualizador()

    def agrupar(self):
        """Agrupa todas as figuras selecionadas atualmente em um único Composite."""
        if len(self.figuras_selecionadas) < 2:
            return # Requer pelo menos 2 figuras para agrupar

       
        novo_grupo = Grupo(list(self.figuras_selecionadas))
        
        
        for fig in self.figuras_selecionadas:
            if fig in self.figuras:
                self.figuras.remove(fig)

        
        self.figuras.append(novo_grupo)
        
     
        self.figuras_selecionadas = [novo_grupo]
        self.atualizar_visualizador()

    def desagrupar(self):
        """Caso a figura selecionada seja um Grupo, desfaz o agrupamento."""
        grupos_para_desfazer = [fig for fig in self.figuras_selecionadas if isinstance(fig, Grupo)]
        
        if not grupos_para_desfazer:
            return

        for grupo in grupos_para_desfazer:
            # Remove o grupo da tela
            if grupo in self.figuras:
                self.figuras.remove(grupo)
            
            # Devolve as partes originais para a lista geral
            for fig_filha in grupo.figuras:
                self.figuras.append(fig_filha)
            
        self.figuras_selecionadas.clear()
        self.atualizar_visualizador()

    def salvar(self):
        caminho = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if caminho:
            dados = [fig.to_dict() for fig in self.figuras]
            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump(dados, f, indent=4)

    def abrir(self):
        caminho = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if caminho:
            with open(caminho, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            mapeamento = {
                "Linha": Linha,
                "Retangulo": Retangulo,
                "Oval": Oval,
                "MaoLivre": MaoLivre,
                "Grupo": Grupo
            }
            
            self.figuras = []
            for item in dados:
                tipo = item.get("tipo")
                if tipo in mapeamento:
                    self.figuras.append(mapeamento[tipo].from_dict(item))
            
            self.figuras_selecionadas.clear()
            self.atualizar_visualizador()
