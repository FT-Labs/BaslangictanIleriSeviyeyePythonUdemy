"""
Author : Arda
Date : 5/11/2020
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout,QApplication,QHBoxLayout,QPushButton


app = QApplication(sys.argv)

pencere = QWidget()
#Set geometry ekran boyutunu ayarlar
pencere.setGeometry(500,500,500,500)
# pencere.setFixedHeight(500)

#setFixedsize ekran boyutunu kısıtlar
# pencere.setFixedSize(500,500)
pencere.setWindowTitle("Merhaba Dünya!")

#QLabel normal yazı çıkartır
#CSS -> cascading style sheet
merhabaDunya = QLabel("Merhaba Dünya!")

merhabaDunya.setStyleSheet("""
QLabel {
color : blue;
background-color : yellow;
font-size : 25px;
margin-left : 100px;
margin-bottom : 120px;
border : 3px black ;
border-style : solid;
}
""")

merhabaDunyaIki = QLabel("Merhaba Dünya 2!")
dikeyLayout = QVBoxLayout()
# pencere.setStyleSheet("""
# QLabel {
# color : blue;
# background-color : yellow;
# font-size : 25px;
# margin-left : 100px;
# margin-bottom : 120px;
# border : 3px black ;
# border-style : solid;
# }
# """)


dikeyLayout.addWidget(merhabaDunya,0,Qt.AlignCenter)
dikeyLayout.addWidget(merhabaDunyaIki,0,Qt.AlignCenter)
# yatayLayout = QHBoxLayout()
# yatayLayout.addWidget(merhabaDunya)
# yatayLayout.addWidget(merhabaDunyaIki)

banaTikla = QPushButton("Bana Tıkla!")
banaTikla.setStyleSheet("""
QPushButton {
color : blue;
background-color : yellow;
font-size : 20px;
border : 3px purple;
border-style : solid;
}
""")

dikeyLayout.addWidget(banaTikla)

pencere.setLayout(dikeyLayout)
# pencere.setLayout(yatayLayout)
pencere.show()
sys.exit(app.exec_())

