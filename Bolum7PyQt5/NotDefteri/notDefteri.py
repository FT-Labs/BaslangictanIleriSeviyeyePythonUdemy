"""
Author : Arda
Date : 5/12/2020
"""

import sys
from PyQt5.QtWidgets import QPlainTextEdit,QApplication,QMainWindow,QPushButton,QWidget,QFileDialog
from PyQt5.QtCore import Qt
from PyQt5 import uic


arayuzYolu = "notdefteri.ui"

Ui_Pencere , QtBaseClass = uic.loadUiType(arayuzYolu)

class Pencere(QMainWindow, Ui_Pencere):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_Pencere.__init__(self)
        self.setupUi(self)

        self.pushTemizle.clicked.connect(self.temizle)
        self.pushKaydet.clicked.connect(self.kaydetButon)
        self.aksiyonKaydet.triggered.connect(self.kaydetButon)
        self.aksiyonAc.triggered.connect(self.AksiyonAc)
        self.aksiyonFarkliKaydet.triggered.connect(self.FarkliKaydet)

    def AksiyonAc(self):
        dosya = QFileDialog.getOpenFileName(self,"Dosya Aç")
        with open(dosya[0], "r", encoding="utf-8") as dosyam:
            yazi = dosyam.read()
            self.yaziEdit.setPlainText(yazi)

    def FarkliKaydet(self):
        dosya = QFileDialog.getSaveFileName(self, "Farklı Kaydet", filter="(Txt Files (*.txt))")
        with open(dosya[0],"w",encoding="utf-8") as dosyam:
            yazi = self.yaziEdit.toPlainText()
            dosyam.write(yazi)

    def temizle(self):
        self.yaziEdit.setPlainText("")

    def kaydetButon(self):
        with open("yazim.txt", "w" , encoding="utf-8") as dosyam:
            yazi = self.yaziEdit.toPlainText()
            dosyam.write(yazi)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())