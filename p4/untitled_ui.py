# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(304, 183)
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(50, 40, 82, 17))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(120, 40, 82, 17))
        self.radioButton_3 = QRadioButton(Form)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(190, 40, 82, 17))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 141, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 70, 161, 16))
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(110, 100, 91, 22))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 140, 75, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"Ingles", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"Frances", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u" Portugues", None))
        self.label.setText(QCoreApplication.translate("Form", u"Seleccione su idioma:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Seleccione el mensaje a mostrar:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"Saludar", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Despedirse", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"Perdon", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"Pedir cafe", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Form", u"Cuanto cuesta", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Form", u"Donde queda", None))

        self.pushButton.setText(QCoreApplication.translate("Form", u"Aceptar", None))
    # retranslateUi

