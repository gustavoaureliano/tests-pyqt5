import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QScrollArea, QFrame, QVBoxLayout, QFormLayout, QGridLayout, QPushButton, QComboBox, QLineEdit
from PyQt5.QtCore import Qt
from math import ceil

from testeFlow import FlowLayout

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self._centralwidget = QWidget()
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        estiloBtn = """
        QPushButton {
            background-color: #004040;
            color: #00EE77;
            font: bold;
            font-size: 22px;
            border-radius: 5px;
            padding: 5px 10px;
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

        self.le_nquest = QLineEdit()
        self.le_nquest.setPlaceholderText("Nº de questões da prova")
        self.le_nquest.setStyleSheet("border: 1px solid red")

        self.btn = QPushButton("Add")
        self.btn.setStyleSheet(estiloBtn)
        self.btn.clicked.connect(lambda: self.setQuest(int(self.le_nquest.text() if self.le_nquest.text() != '' else 0)))

        self.layoutCb = QFormLayout()
        self.layoutCb.setAlignment(Qt.AlignCenter)
        self.layoutCb.addRow("Oi", QComboBox())



        self.layout_grid = QGridLayout()
        self.layout_grid.setAlignment(Qt.AlignCenter)


        #self.grid.setStyleSheet("border: 1px solid lime")

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(False)
        self.scroll.setAlignment(Qt.AlignCenter)


        self.layout.addWidget(self.le_nquest)
        self.layout.addWidget(self.btn)

        self.wid = QWidget()
        self.layout_flow = FlowLayout(self.wid)
        self.layout_flow.setAlignment(Qt.AlignCenter)
        self.layout_flow.setContentsMargins(40,0,20,0)
        cont = 0
        for n in range(90):
            cont += 1
            form_layout = QFormLayout()
            form_layout.setAlignment(Qt.AlignCenter)
            form = QFrame()
            form.setLayout(form_layout)
            alternativa = QComboBox()
            alternativa.addItems(["A", "B", "C", "D", "E"])
            alternativa.setStyleSheet("""
            QComboBox{ 
                background-color: #004040; 
                color: #00EE77;
                #border-radius: 5px;
                padding: 5px;
                #border: 1px solid #00EE77;
            }
            QComboBox::down-arrow {
                #border : 4px black;
                #border-style : dotted;
                color: red;
            }
            """)
            form_layout.addRow(f'{cont:2}#', alternativa)
            self.layout_flow.addWidget(form)
            self.layout_flow.addWidget(form)
        #self.layout.addLayout(self.layout_flow)
        self.scroll.setWidget(self.wid)
        #self.layout.addWidget(self.scroll)
        self.layout.addWidget(self.wid)

        #self.layout.addLayout(self.layout_grid)
        #self.layout.addWidget(self.grid)

        self._centralwidget.setLayout(self.layout)
        #self._centralwidget.setStyleSheet("border: 1px solid blue")

        self.resize(600,400)
        self.setWindowTitle("Add widget")
        self.setCentralWidget(self._centralwidget)

    def setQuest(self, num_quests):
        cont = 0
        for n in range(num_quests):
            form_layout = QFormLayout()
            form_layout.setAlignment(Qt.AlignCenter)
            form = QFrame()
            form.setLayout(form_layout)
            alternativa = QComboBox()
            alternativa.addItems(["A", "B", "C", "D", "E"])
            form_layout.addRow(f'{cont:2}', alternativa)
            self.layout_flow.addWidget(form)

    #def setQuest(self, num_quests):
    #    #if num_quests <
    #    rj = 9
    #    ri = ceil(num_quests / rj)
    #    cont = 0
    #    self.clearLayout(self.layout_grid)
    #    for j in range(rj):
    #        for i in range(ri):
    #            cont += 1
    #            if cont <= num_quests and num_quests != 0:
    #                form_layout = QFormLayout()
    #                form_layout.setAlignment(Qt.AlignCenter)
    #                form = QFrame()
    #                # form.setStyleSheet("padding: 0px 5px; border: 1px solid red;")
    #                form.setLayout(form_layout)
    #                alternativa = QComboBox()
    #                alternativa.addItems(["A", "B", "C", "D", "E"])
    #                form_layout.addRow(f'{cont:2}', alternativa)
    #                self.layout_grid.addWidget(form, j, i)
    #                print(i, j)
    #    self.grid = QWidget()
    #    self.grid.setLayout(self.layout_grid)
    #    self.scroll.setWidget(self.grid)

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Janela()
    window.show()
    sys.exit(app.exec())