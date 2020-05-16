"""
Author : Arda
Date : 5/11/2020
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QLabel,QRadioButton,QWidget

class Pencere(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setFixedSize(500,500)
        self.setWindowTitle("Radio Butonları")

        self.dikeyLayout = QVBoxLayout()

        self.setStyleSheet("""
        QRadioButton{
        font-size : 12px;
        color : red;
        margin-left : 25px;
        margin-bottom : 30px;
        }
        """)

        labelSoru = QLabel("Aşağıdakilerden Hangi Yazılım Dilini Tercih Edersiniz?")

        labelSoru.setStyleSheet("""
        QLabel{
        font-size : 15px;
        color : blue;
        border : 3px black;
        border-style : solid;
        font-weight : bold;
        }
        """)

        self.dikeyLayout.addWidget(labelSoru,0,Qt.AlignCenter)

        self.radioPython = QRadioButton("Python")
        self.dikeyLayout.addWidget(self.radioPython,0,Qt.AlignTop)

        self.radioKotlin = QRadioButton("Kotlin")
        self.dikeyLayout.addWidget(self.radioKotlin, 0, Qt.AlignTop)

        self.radioJavaScript = QRadioButton("JavaScript")
        self.dikeyLayout.addWidget(self.radioJavaScript, 0, Qt.AlignTop)

        self.radioC = QRadioButton("C")
        self.dikeyLayout.addWidget(self.radioC, 0, Qt.AlignTop)

        self.labelCevap = QLabel("")
        self.labelCevap.setStyleSheet("""
        QLabel{
        font-size : 15px;
        font-family : Arial, Helvetica ,sans-serif;
        color : blue; 
        font-style : italic;
        }
        """)
        self.dikeyLayout.addWidget(self.labelCevap, 0, Qt.AlignTop)

        self.setLayout(self.dikeyLayout)

        self.radioPython.toggled.connect(self.radioTiklandi)
        self.radioC.toggled.connect(self.radioTiklandi)
        self.radioKotlin.toggled.connect(self.radioTiklandi)
        self.radioJavaScript.toggled.connect(self.radioTiklandi)


    def radioTiklandi(self):

        if self.radioPython.isChecked():
           self.labelCevap.setText("Python mı? Güzel Tercih!!")
        if self.radioJavaScript.isChecked():
            self.labelCevap.setText("Javascript pek bilmiyorum, fakat web programlama bana göre değil.")
        if self.radioKotlin.isChecked():
            self.labelCevap.setText("Güzel Tercih, Java'dan Daha Güzel Olduğu Kesin :)")
        if self.radioC.isChecked():
            self.labelCevap.setText("C mi? En zorunu başarabiliyorsan tebrik ederim.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Radio Butonları Programı")
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())









