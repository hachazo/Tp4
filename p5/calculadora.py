import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTextBrowser, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLCDNumber
#from PyQt5 import QtCore, QtGui, QtWidgets

class CalculatorApp(QMainWindow,QWidget):
    def __init__(self):
        super().__init__()
        self.ventana_principal()

    def ventana_principal(self):
        self.layout = QVBoxLayout() # Organiza los widget
        self.centralWidget = QWidget() # ventana principal
        self.setCentralWidget(self.centralWidget)
        self.setWindowTitle("Calculadora")
        self.botones_vl = QVBoxLayout()  # Almacena total de botones en vertical

        self.texto_pantalla_h = QHBoxLayout()
        self.texto_pantalla = QTextBrowser()
        self.texto_pantalla_h = QHBoxLayout()
        self.texto_pantalla_h.addWidget(self.texto_pantalla)
        self.botones_vl.addLayout(self.texto_pantalla_h)
    
        self.botones_h1= QHBoxLayout()
        boton1 = ["7", "8", "9", "/"]
        for boton in boton1:
            self.botones_h1.addWidget(self.crear_boton(boton))
        self.botones_vl.addLayout(self.botones_h1)

        self.botones_h2= QHBoxLayout()
        boton2 = ["4", "5", "6", "*"]
        for boton in boton2:
            self.botones_h2.addWidget(self.crear_boton(boton))
        self.botones_vl.addLayout(self.botones_h2)
        
        self.botones_h3= QHBoxLayout()
        boton3 = ["1", "2", "3", "+"]
        for boton in boton3:
            self.botones_h3.addWidget(self.crear_boton(boton))
        self.botones_vl.addLayout(self.botones_h3)
        
        self.botones_h4= QHBoxLayout()
        boton4 = ["0", ".", "=", "-"]
        for boton in boton4:
            self.botones_h4.addWidget(self.crear_boton(boton))
        self.botones_vl.addLayout(self.botones_h4)
        
        self.layout.addLayout(self.botones_vl) # Agrega botones_v1 a layout
        self.centralWidget.setLayout(self.layout) # Agrega en layou a la ventnana principal
    
    def crear_boton(self, text):
        button = QPushButton(text)
        button.clicked.connect(lambda x=text: self.calcular(text)) # Agrega una aciccion al boton
        return button
    
    def calcular(self,text):
    
        if text == "+" or text == "-" or text == "*" or text == "%":
            self.texto_pantalla.clear()
            operacion = text
            print(operacion)
            
        if text != "=" and not self.texto_pantalla.toPlainText():
            if text != "+" and text != "-" and text != "*" and text != "%" and text != "=":
                self.texto_pantalla.append(text)
                operando1 =text      
                print(operando1)
        else:        
            if self.texto_pantalla.toPlainText():
                if text != "+" and text != "-" and text != "*" and text != "%" and text != "=":
                    self.texto_pantalla.append(text)
                    operando2 = text
            if text == "=" and operando1 and operando2:
                print("terminado")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())