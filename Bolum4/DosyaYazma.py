"""
Author : Arda
Date : 4/17/2020
"""

# "w" : Write (Yaz komutu) , "a" : Append (dosyanın en son bittiği yerden yazmaya başla)
# ASCII : Amerikan standardı , utf-8 : türkçeye uygun

# dosyam = open("ilkdosyam.txt" , "a" , encoding="utf-8")
# ilkYazim = "Merhaba! Bu benim dosyaya ilk yazı yazdırışım.\nBu da benim 2.satırım.\nBu da bir tab karakteri: \t"
# dosyam.write(ilkYazim)
# dosyam.close()

meyveler = ["portakal" , "çilek" , "muz" , "kivi" , "elma"]

with open("ikincidosyam.txt" , "w" , encoding= "utf-8") as dosyam:
    dosyam.writelines(meyveler)



