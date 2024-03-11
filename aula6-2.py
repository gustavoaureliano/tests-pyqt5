import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5 import QtGui, QtCore

class Janela(QMainWindow):
    def  __init__(self, parent=None):
        super().__init__(parent)
        self.topo = 500
        self.esquerda = 500
        self.altura = 400
        self.largura = 600
        self.titulo = "Caixa de texto"

        estiloBtn1 = """
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
        """

        estiloBtn2 = """
        QPushButton {
            background-color: #400000;
            color: #EE0077;
            font: bold;
            font-size: 22px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #500000;
            color: #FF0088;
        }
        QPushButton:pressed {
            background-color: #EE0077;
            color: #400000;
        }
        """

        estiloBtn3 = """
        QPushButton {
            background-color: #000040;
            color: #0077EE;
            font: bold;
            font-size: 22px;
            border-radius: 5px;
        }
        QPushButton:hover {
            background-color: #000050;
            color: #0088FF;
        }
        QPushButton:pressed {
            background-color: #0077EE;
            color: #000040;
        }
        """

        btn1 = QPushButton("Carro 1", self)
        btn1.setStyleSheet(estiloBtn1)
        btn1.move(25, 170)
        btn1.resize(150, 60)
        btn1.clicked.connect(lambda: self.changeText("Carro 1 foi selecionado", "#00EE77", './imgs/carro1.png'))

        btn2 = QPushButton("Carro 2", self)
        btn2.setStyleSheet(estiloBtn2)
        btn2.move(225, 170)
        btn2.resize(150, 60)
        btn2.clicked.connect(lambda: self.changeText("Carro 2 foi selecionado", "#EE0077", "./imgs/carro2.png"))

        btn3 = QPushButton("Botão texto", self)
        btn3.setStyleSheet(estiloBtn3)
        btn3.move(425, 170)
        btn3.resize(150, 60)
        btn3.clicked.connect(lambda: self.lbl_texto.setText(f"Digitou: {self.lineEdit.text()}"))

        self.lbl1 = QLabel(self)
        self.lbl1.move(60, 0)
        self.lbl1.resize(400, 170)
        self.lbl1.setText("Aperte um botão")
        self.lbl1.setStyleSheet("QLabel { font-weight: bold; font-size: 20px; }")

        self.lbl_texto = QLabel(self)
        self.lbl_texto.move(320, 0)
        self.lbl_texto.resize(280, 170)
        self.lbl_texto.setText("Digitou: ")
        self.lbl_texto.setStyleSheet("QLabel { font-weight: bold; font-size: 20px; }")

        self.carro = QLabel(self)
        self.carro.move(75, 230)
        self.carro.resize(600, 170)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(55, 30)
        self.lineEdit.resize(150, 25)
        self.setStyleSheet("QLineEdit { font-size: 14px; border: 1px solid black; border-radius: 7px; padding: 0px 5px }")

        self.carregarJanela()

    def changeText(self, texto, cor, imgPath):
        self.lbl1.setText(texto)
        self.lbl1.setStyleSheet("QLabel { font-weight: bold; font-size: 20px; color:" + cor + ";}")
        pixmap = QtGui.QPixmap(imgPath).scaled(450, 450, QtCore.Qt.KeepAspectRatio)
        self.carro.setPixmap(pixmap)

    def carregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    sys.exit(app.exec())
