"""
Author : Arda
Date : 5/11/2020
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox,QLabel,QVBoxLayout,QPushButton


class MesajKutusu(QMessageBox):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.setWindowTitle("Mesaj Kutusu")
        self.setText("Tebrikler! Butona bastınız.")


class Pencere(QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowTitle("Buton Özelliği")
        self.setFixedSize(300,300)

        self.dikeyLayout = QVBoxLayout()
        self.banaBasButon = QPushButton("Bana Tıkla!")
        self.banaBasButon.setStyleSheet("""
        QPushButton{
        font-size : 17px;
        color : blue;
        background : yellow;
        }
        """)

        self.basmaSayisi = 0
        self.basLabel = QLabel("Bana 0 kere basıldı.")
        self.dikeyLayout.addWidget(self.basLabel,0,Qt.AlignCenter)

        self.dikeyLayout.addWidget(self.banaBasButon)
        self.setLayout(self.dikeyLayout)

        self.mesajKutusu = MesajKutusu()
        self.banaBasButon.clicked.connect(self.butonaBasildi)

    def butonaBasildi(self):
        self.mesajKutusu.show()
        self.basmaSayisi += 1
        self.basLabel.setText(f"Bana {self.basmaSayisi} kere basıldı.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("ButonProgrami")
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())