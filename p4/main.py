from ventana import Main
from ventana_2 import Ui_ventana_2
from PyQt5 import QtWidgets
import sys

class Conectar_ventanas(Main):
    def __init__(self,form):
        super().__init__(form)
    
        self.boton_precionado()
    def boton_precionado(self):
        if form.precionado() == True:
            ventana_2 = QtWidgets.QWidget()
            ui = Ui_ventana_2()
            ui.setupUi(ventana_2)
            ventana_2.show()  
                     
app = QtWidgets.QApplication(sys.argv)
form = QtWidgets.QWidget()                                  
ui = Conectar_ventanas(form)
form.show()

# conectar_ventanas(form)
sys.exit(app.exec_())