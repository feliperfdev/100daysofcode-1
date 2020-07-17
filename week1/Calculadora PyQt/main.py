import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QSizePolicy, QLineEdit
from math import factorial

class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400, 400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.setCentralWidget(self.cw)
        self.setStyleSheet(
            '* {background: #1e4c52; color: white; font-weight: 700;}'
        )

        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        # .addWidget(widget, linha, coluna, linha_expansão, coluna_expansão)
        self.display.setDisabled(True)
        self.display.setStyleSheet(
            '* {background: #0f93a5; color: #000; font-size: 30px;}'
        )
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # ajusta tamanho do display à medida em que objetos são adicionados nas linhas e colunas...
        # ...da matriz que forma o design da calculadora

#=========================================== BOTÕES ===========================================
        self.add_btn(QPushButton('7'), 1, 0, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('8'), 1, 1, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('9'), 1, 2, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('AC'), 1, 3, 1, 1,
                     lambda: self.display.setText(''), #seta o display para texto vazio
                     'background: #e44c0c; color: #fff; font-weight: 700;'
                     )
        self.add_btn(QPushButton('<<'), 1, 4, 1, 1,
                     lambda: self.display.setText(self.display.text()[:-1]),
                     #apaga o último carctere da operação que está sendo digitada
                     'background: #20b050; color: #fff; font-weight: 700;'
                     )

        self.add_btn(QPushButton('4'), 2, 0, 1, 1, None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('5'), 2, 1, 1, 1, None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('6'), 2, 2, 1, 1, None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('+'), 2, 3, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('-'), 2, 4, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')

        self.add_btn(QPushButton('1'), 3, 0, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('2'), 3, 1, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('3'), 3, 2, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('*'), 3, 3, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('/'), 3, 4, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')

        self.add_btn(QPushButton('.'), 4, 0, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('0'), 4, 1, 1, 1,None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('='), 4, 2, 1, 1,
                     self.eval_igual, 'background: #4c4c4c; color: #fff; font-weight: 700;'
                     )
        self.add_btn(QPushButton(''), 4, 3, 1, 1, None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
        self.add_btn(QPushButton('**'), 4, 4, 1, 1, None,
                     'background: #1b3456; color: #fff; font-weight: 700;')
#===============================================================================================

#=========================================== FUNÇÕES ===========================================
    def add_btn(self, btn, row, col, rowspan, colspan, function=None, style=None):
        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not function:
            btn.clicked.connect( # ao ser clicado, o botão fará:
                lambda: self.display.setText(self.display.text() + btn.text())
                #no display, ele vai setar o texto para o texto que está escrito no botão
        )
        else:
            btn.clicked.connect(function)

        if style:
            btn.setStyleSheet(style)

        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        #ajusta tamanho dos botões à medida em que vão ocupando as linhas e colunas...
        #...da matriz que forma o design da calculadora

    def eval_igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text())) #avalia a conta que está no display
            )
        except OverflowError:
            self.display.setText('Conta muito grande!')
        except SyntaxError:
            self.display.setText('Erro!')
        except SystemError:
            self.display.setText('Erro!')

#===============================================================================================

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
