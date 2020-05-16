"""
Author : Arda
Date : 5/1/2020
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


#Kullanıcı adı ve şifreyi yazın.

gonderen_kullaniciAdi = "udemydeneme5@gmail.com"
gonderen_sifre = "123654Aa"

alan_kullaniciAdi = "udemydeneme5@gmail.com"

#MIME (Maili kurmak için)

mesaj = MIMEMultipart()
mesaj["From"] = gonderen_kullaniciAdi
mesaj["To"] = alan_kullaniciAdi
mesaj["Subject"] = "Otomatik Mail Atmayı Öğreniyorum!"
mesaj_icerigi = """Merhaba,
Python ile otomatik mail atmayı öğreniyorum.
***********************************
"""
mesaj.attach(MIMEText(mesaj_icerigi , "plain"))
yollanacakEk_dosya_yolu = "MailEki.docx"
ek_dosyasi = open(yollanacakEk_dosya_yolu , "rb")
payload = MIMEBase('application' , 'octate-stream')
payload.set_payload((ek_dosyasi).read())
encoders.encode_base64(payload)
#EK DOSYASINA HEADER (YOLLANACAK DOSYA ADI) YOLLAMAZSANIZ EKİ DÜZGÜN YOLLAMAZ!!!
payload.add_header("Content-Disposition" , "OtomatikEkYolluyorum" , filename = yollanacakEk_dosya_yolu)
mesaj.attach(payload)


SMTP = smtplib.SMTP("smtp.gmail.com" , 587)
SMTP.starttls()  #Şifreli güvenlik
SMTP.login(gonderen_kullaniciAdi , gonderen_sifre)
text = mesaj.as_string()
SMTP.sendmail(gonderen_kullaniciAdi , alan_kullaniciAdi , text)
SMTP.quit()

print("Mail başarıyla gönderildi!")



