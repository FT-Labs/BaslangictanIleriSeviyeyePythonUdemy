"""
Author : Arda
Date : 5/14/2020
"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

uiYolu = "HesapMakinesi.ui"

Ui_Widget, Qt_BaseClass = uic.loadUiType(uiYolu)


class HesapMakinesiWidget(Ui_Widget, QWidget):

    def __init__(self):
        QWidget.__init__(self)
        Ui_Widget.__init__(self)
        self.setupUi(self)

        self.buton0.clicked.connect(lambda: self.sayiyiEkle("0"))
        self.buton1.clicked.connect(lambda: self.sayiyiEkle("1"))
        self.buton2.clicked.connect(lambda: self.sayiyiEkle("2"))
        self.buton3.clicked.connect(lambda: self.sayiyiEkle("3"))
        self.buton4.clicked.connect(lambda: self.sayiyiEkle("4"))
        self.buton5.clicked.connect(lambda: self.sayiyiEkle("5"))
        self.buton6.clicked.connect(lambda: self.sayiyiEkle("6"))
        self.buton7.clicked.connect(lambda: self.sayiyiEkle("7"))
        self.buton8.clicked.connect(lambda: self.sayiyiEkle("8"))
        self.buton9.clicked.connect(lambda: self.sayiyiEkle("9"))
        self.butonNokta.clicked.connect(lambda: self.sayiyiEkle("."))

        self.butonEsittir.clicked.connect(lambda: self.bekleyenIslem("="))
        self.butonCikart.clicked.connect(lambda: self.bekleyenIslem("-"))
        self.butonCarp.clicked.connect(lambda: self.bekleyenIslem("*"))
        self.butonBol.clicked.connect(lambda: self.bekleyenIslem("/"))
        self.butonTopla.clicked.connect(lambda: self.bekleyenIslem("+"))

        self.ilkSayi = ""
        self.yapilacakIslem = ""

    def bekleyenIslem(self, butonIslem):
        self.labelBekleyenIslem.setText(butonIslem)

        if self.islemEdit.text() == "":
            self.yapilacakIslem = butonIslem
        else:
            if self.ilkSayi == "":
                self.ilkSayi = float(self.islemEdit.text())
                self.yapilacakIslem = butonIslem
                self.islemEdit.setText("")
                self.cevapEdit.setText(str(self.ilkSayi))
            else:
                if self.yapilacakIslem == "=":
                    self.yapilacakIslem = butonIslem

                if self.yapilacakIslem == "+":
                    self.ilkSayi += float(self.islemEdit.text())
                    self.islemEdit.setText("")
                    self.cevapEdit.setText(str(self.ilkSayi))
                    self.yapilacakIslem = butonIslem
                elif self.yapilacakIslem == "-":
                    self.ilkSayi -= float(self.islemEdit.text())
                    self.islemEdit.setText("")
                    self.cevapEdit.setText(str(self.ilkSayi))
                    self.yapilacakIslem = butonIslem
                elif self.yapilacakIslem == "*":
                    self.ilkSayi *= float(self.islemEdit.text())
                    self.islemEdit.setText("")
                    self.cevapEdit.setText(str(self.ilkSayi))
                    self.yapilacakIslem = butonIslem
                elif self.yapilacakIslem == "/":
                    if float(self.islemEdit.text()) == 0.:
                        self.islemEdit.setText("")
                    else:
                        self.ilkSayi /= float(self.islemEdit.text())
                        self.islemEdit.setText("")
                        self.cevapEdit.setText(str(self.ilkSayi))
                        self.yapilacakIslem = butonIslem
                elif self.yapilacakIslem == "=":
                    self.ilkSayi = float(self.islemEdit.text())
                    self.cevapEdit.setText(str(self.ilkSayi))
                    self.islemEdit.setText("")
                    self.yapilacakIslem = butonIslem

    def sayiyiEkle(self, butonSayi):
        islemEditSayilar = self.islemEdit.text()
        self.islemEdit.setText(islemEditSayilar + butonSayi)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("HesapMakinesi")
    hesapMakinesi = HesapMakinesiWidget()
    hesapMakinesi.show()
    sys.exit(app.exec_())
