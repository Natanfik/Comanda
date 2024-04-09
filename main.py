from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt6.QtCore import QUrl
from PyQt6.uic import *
import sys


def abrir_pedido():
    tela_pedido.show()
    tela_mesa.close()

def abrir_mesas():
    tela_pedido = QWebEngineView()
    profile = tela_pedido.page().profile()
    tela_mesa.show()
    tela_pedido.close()
    profile.clearHttpCache()





app = QApplication(sys.argv)

window = QWidget() # criando tela uic

#declarando telas  
tela_pedido = loadUi('tela_pedido.ui')
tela_mesa = loadUi('tela_mesas.ui')

#conectando nas telas
tela_pedido.comboBox.addItems(["Nenhum","Calabresa","Lombinho", "Quatro Queijos", "Frango", "Sensação", "chocolate"])
tela_pedido.comboBox_3.addItems(["Nenhum","Calabresa","Lombinho", "Quatro Queijos", "Frango", "Sensação", "chocolate"])
tela_pedido.comboBox_5.addItems(["Nenhum","Calabresa","Lombinho", "Quatro Queijos", "Frango", "Sensação", "chocolate"])
tela_pedido.borda.addItems(["Nenhum","Catupery", "Chocolate"])
tela_pedido.tamanho.addItems(["GG", "G", "P"])
tela_mesa.pushButton.clicked.connect(abrir_pedido) #para abrir tela de pedido
tela_mesa.pushButton_2.clicked.connect(abrir_pedido)
tela_mesa.pushButton_3.clicked.connect(abrir_pedido)
tela_mesa.pushButton_4.clicked.connect(abrir_pedido)
tela_mesa.pushButton_5.clicked.connect(abrir_pedido)
tela_mesa.pushButton_6.clicked.connect(abrir_pedido)
tela_mesa.pushButton_7.clicked.connect(abrir_pedido)
tela_mesa.pushButton_8.clicked.connect(abrir_pedido)
tela_mesa.pushButton_9.clicked.connect(abrir_pedido)
tela_mesa.pushButton_10.clicked.connect(abrir_pedido)
tela_mesa.pushButton_11.clicked.connect(abrir_pedido)
tela_mesa.pushButton_12.clicked.connect(abrir_pedido)
tela_mesa.pushButton_13.clicked.connect(abrir_pedido)
tela_mesa.pushButton_14.clicked.connect(abrir_pedido)
tela_mesa.pushButton_15.clicked.connect(abrir_pedido)
tela_mesa.pushButton_16.clicked.connect(abrir_pedido)
tela_pedido.finalizar.clicked.connect(abrir_mesas)

tela_mesa.show() #mostrar tela primária
app.exec()

