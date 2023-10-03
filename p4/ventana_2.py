from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventana_2(object):
    def setupUi(self, ventana_2):
        ventana_2.setObjectName("ventana_2")
        ventana_2.resize(180, 145)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label = QtWidgets.QLabel(ventana_2)
        self.label.setGeometry(QtCore.QRect(40, 20, 121, 16))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.traduccion = QtWidgets.QLabel(ventana_2)
        self.traduccion.setGeometry(QtCore.QRect(30, 60, 141, 20))
        self.traduccion.setFont(font)
        self.traduccion.setObjectName("traduccion")
        self.aceptar_1 = QtWidgets.QPushButton(ventana_2)
        self.aceptar_1.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.aceptar_1.setFont(font)
        self.aceptar_1.setObjectName("aceptar_1")

        self.retranslateUi(ventana_2)

    def retranslateUi(self, ventana_2):
        ventana_2.setWindowTitle("Idioma")
        self.label.setText("Su traducción es: ")
        self.traduccion.setText("ddfdfdfd")
        self.aceptar_1.setText("Aceptar")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_2 = QtWidgets.QWidget()
    ui = Ui_ventana_2()
    ui.setupUi(ventana_2)
    ventana_2.show()
    sys.exit(app.exec_())
