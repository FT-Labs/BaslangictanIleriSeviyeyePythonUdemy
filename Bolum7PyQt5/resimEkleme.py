"""
Author : Arda
Date : 5/11/2020
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtGui import QPixmap


app = QApplication(sys.argv)

pencere = QWidget()
pencere.setWindowTitle("Türk Bayrağı")
pencere.setGeometry(0, 0, 150, 150)

dikeyLayout = QVBoxLayout()
resim = QPixmap("turkbayragi.png")
resimLabel = QLabel()
resimLabel.setPixmap(resim)
dikeyLayout.addWidget(resimLabel,0,Qt.AlignCenter)

neMutlu = QLabel("Ne Mutlu Türküm Diyene!")

#font-style -> font-family olacak.
neMutlu.setStyleSheet("""
QLabel {
font-size : 25px;
font-family : "Times New Roman", Times, serif;
color : red;
}
""")
dikeyLayout.addWidget(neMutlu,0,Qt.AlignCenter)
pencere.setLayout(dikeyLayout)

pencere.show()

sys.exit(app.exec_())