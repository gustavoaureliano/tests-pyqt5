import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 500
        self.esquerda = 500
        self.altura = 400
        self.largura = 600
        self.titulo = "Botões"

        btn1 = QPushButton("Botão 1", self)
        btn1.move(75, 170)
        btn1.resize(150, 60)
        btn1.setStyleSheet("""
        QPushButton {
            background-color: #004040;
            color: #00EE77;
            font: bold;
            font-size: 22px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #005050;
            color: #00FF88;
        }
        QPushButton:pressed {
            background-color: #00EE77;
            color: #004040;
        }
        """)
        btn1.clicked.connect(lambda: print("Botão 1 pressionado!"))

        btn2 = QPushButton("Botão 2", self)
        btn2.move(375, 170)
        btn2.resize(150, 60)
        btn2.setStyleSheet("QPushButton { background-color: #400000; color: #EE0077; font: bold; font-size: 22px; border-radius: 5px; }")
        btn2.clicked.connect(lambda: print("Botão 2 pressionado!"))

        self.carregarJanela()

    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    sys.exit(app.exec())
