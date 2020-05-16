"""
Author : Arda
Date : 5/15/2020
"""

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QTabWidget,QPushButton,QLineEdit,QLabel
import time
from threading import Thread
from Bolum7PyQt5.EmailProgrami.EmailSQL import EmailYolla,MySQLKullanicilar
import math
from email.mime.multipart import MIMEMultipart

uiYolu = "emailProgrami.ui"

Ui_EmailProgrami , Qt_BaseClass = uic.loadUiType(uiYolu)

class EmailProgrami(QMainWindow, Ui_EmailProgrami):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.emailYolla = EmailYolla()
        self.mysqlKullanicilar = MySQLKullanicilar()

        self.sifreEdit.setEchoMode(QLineEdit.Password)
        self.aksiyonCikisYap.triggered.connect(self.cikisYap)

        self.butonGirisYap.clicked.connect(self.girisYap)
        self.pushGonder.clicked.connect(self.emailiGonder)
        self.yanlisGiris = 0


    def emailiGonder(self):
        self.emailYolla.mesaj = MIMEMultipart()

        self.emailYolla.kullanici_emaili = self.emailEdit.text()
        self.emailYolla.kullanici_sifre = self.sifreEdit.text()

        self.emailYolla.mesajOlustur(self.kimeMailEdit.text(),self.konuEdit.text(),self.mesajEdit.toPlainText())
        adet = self.spinMesajSayisi.value()

        cevap = self.emailYolla.emailYolla(adet)

        if cevap:
            self.labelGonderildi.setStyleSheet("""
            QLabel{color : green;}
            """)
            self.labelGonderildi.setText("Mailiniz başarıyla gönderildi.")
        else:
            self.labelGonderildi.setStyleSheet("""
            QLabel{color : red;}
            """)
            self.labelGonderildi.setText("Mail içeriğinizde hatalar var. Lütfen düzeltin.")

    def girisYap(self):
        email = self.emailEdit.text()
        sifre = self.sifreEdit.text()

        if self.mysqlKullanicilar.girisKontrolu(email,sifre):
            self.emailEdit.setDisabled(True)
            self.sifreEdit.setDisabled(True)

            self.labelHata.setStyleSheet("""
            QLabel{color : green;}
            """)
            time.sleep(0.2)
            self.labelHata.setText("Başarıyla Giriş Yapıldı!")

        else:
            self.labelHata.setStyleSheet("""
            QLabel{color : red;}
            """)
            self.yanlisGiris += 1
            self.labelHata.setText(f"Hatalı kullanıcı emaili veya şifre. Yanlış giriş sayısı {self.yanlisGiris}.")

            if self.yanlisGiris %3 == 0:
                self.emailEdit.setDisabled(True)
                self.sifreEdit.setDisabled(True)

                thr = Thread(target=self.bekle)
                thr.start()


    def bekle(self):
        suanki_zaman = time.time()

        while True:
            beklemeSuresi = 5
            simdiki_zaman = time.time()
            fark = simdiki_zaman-suanki_zaman

            kalanSure = math.ceil(beklemeSuresi - fark)
            self.labelHata.setText(f"{self.yanlisGiris} kere hatalı giriş yapıldı. {kalanSure} saniye bekleniyor.")

            if fark>=5:
                self.labelHata.setStyleSheet("""
                QLabel{color : green;})
                """)
                self.labelHata.setText("Yeniden giriş yapmayı deneyebilirsiniz.")
                self.emailEdit.setDisabled(False)
                self.sifreEdit.setDisabled(False)
                break

    def cikisYap(self):
        sys.exit(app.exec_())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("EmailProgrami")
    emailProg = EmailProgrami()
    emailProg.show()
    sys.exit(app.exec_())