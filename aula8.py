import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QRadioButton, QPushButton, QFrame
from PyQt5.QtCore import Qt


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.largura = 400
        self.altura = 600
        self.titulo = "RadioButton"

        self._centralWidget = QWidget()
        self._centralWidget.setStyleSheet("background-color: #004040")

        self.layout = QVBoxLayout()
        #self.layout.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.layout.setAlignment(Qt.AlignCenter)


        self.lbl_top = QLabel()
        self.lbl_top.setText("Selecione uma cor")
        self.lbl_top.setStyleSheet("color: #00EE77; font-size: 24px; /* border: 1px solid red */")
        self.lbl_top.setAlignment(Qt.AlignCenter)

        self.rb_azul = QRadioButton()
        self.rb_azul.setText("Azul")
        self.rb_azul.setStyleSheet("color: #7777FF; font-size: 18px")

        self.rb_amarelo = QRadioButton()
        self.rb_amarelo.setText("Amarelo")
        self.rb_amarelo.setStyleSheet("color: #FFFF77; font-size: 18px")

        self.rb_verde = QRadioButton()
        self.rb_verde.setText("Verde")
        self.rb_verde.setStyleSheet("color: #77FF77; font-size: 18px; /*border: 1px solid red;*/")

        self.rb_vermelho = QRadioButton()
        self.rb_vermelho.setText("Vermelho")
        self.rb_vermelho.setStyleSheet("color: #FF7777; font-size: 18px; /*border: 1px solid red;*/")


        self.layout_rbtn = QVBoxLayout()
        self.layout_rbtn.setAlignment(Qt.AlignHCenter)
        self.layout_rbtn.addWidget(self.rb_azul)
        self.layout_rbtn.addWidget(self.rb_amarelo)
        self.layout_rbtn.addWidget(self.rb_verde)
        self.layout_rbtn.addWidget(self.rb_vermelho)

        self.fr_rbtns = QFrame()
        self.fr_rbtns.setLayout(self.layout_rbtn)

        estiloBtn = """
        QPushButton {
            background-color: #00EE77;
            color: #004040;
            font: bold;
            font-size: 22px;
            border-radius: 5px;
            padding: 5px 15px;
        }
        QPushButton:hover {
            background-color: #00DD66;
            color: #003030;
        }
        QPushButton:pressed {
            background-color: #004040;
            color: #00EE77;
        }
        """

        self.btn_enviar = QPushButton()
        self.btn_enviar.setText("Enviar")
        self.btn_enviar.setStyleSheet(estiloBtn)
        self.btn_enviar.clicked.connect(self.enviar)

        self.layout_btn = QVBoxLayout()
        self.layout_btn.setAlignment(Qt.AlignCenter)
        self.layout_btn.addWidget(self.btn_enviar)

        self.fr_btn = QFrame()
        self.fr_btn.setLayout(self.layout_btn)

        self.lbl_bottom = QLabel()
        self.lbl_bottom.setText("Cor selecionada: ")
        self.lbl_bottom.setStyleSheet("QLabel { color: #00EE77; font-size: 22px; border: /*1px solid red; */}")

        self.layout.addWidget(self.lbl_top)
        self.layout.addWidget(self.fr_rbtns)
        self.layout.addWidget(self.fr_btn)
        self.layout.addWidget(self.lbl_bottom)

        self._centralWidget.setLayout(self.layout)


        self.setCentralWidget(self._centralWidget)
        self.resize(self.largura, self.altura)
        self.setWindowTitle(self.titulo)

    def enviar(self):
        if self.rb_azul.isChecked():
            self.lbl_bottom.setText("Cor selecionada: Azul")
        elif self.rb_amarelo.isChecked():
            self.lbl_bottom.setText("Cor selecionada: Amarelo")
        elif self.rb_verde.isChecked():
            self.lbl_bottom.setText("Cor selecionada: Verde")
        elif self.rb_vermelho.isChecked():
            self.lbl_bottom.setText("Cor selecionada: Vermelho")


def main():
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
