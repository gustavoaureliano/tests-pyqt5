import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Janela(QMainWindow):

    def __init__(self):
        super().__init__()
        self.topo = 500
        self.esquerda = 500
        self.altura = 400
        self.largura = 600
        self.titulo = "Minha aplicação"
        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Janela()
    sys.exit(app.exec())
