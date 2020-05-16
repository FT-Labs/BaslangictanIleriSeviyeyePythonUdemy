"""
Author : Arda
Date : 4/19/2020
"""


# Herhangi iki kenarın toplamı öbür kenardan daha büyük olmalıdır.

class Ucgen():

    def __init__(self , kenar1 , kenar2 , hipotenus):
        self.kenar1 = kenar1
        self.kenar2 = kenar2
        self.hipotenus = hipotenus

        if self.ucgenMiDegilMi(self.kenar1 , self.kenar2 , self.hipotenus):
            print("Bu bir üçgendir.")
        else:
            raise Exception("Bu bir üçgen değildir.")

        self.hipotenusuBul()
        self.ucgenTipiniBelirle()


    def ucgenTipiniBelirle(self):

        if self.kenar1 == self.kenar2 and self.kenar1 == self.hipotenus:
            print("Bu üçgen bir eşkenar üçgendir.")
        elif self.kenar1 == self.kenar2 or self.kenar1 == self.hipotenus or self.kenar2 == self.hipotenus:
            print("Bu üçgen bir ikizkenar üçgendir.")
        else:
            # Pisagor Teoremi -> kenar1 ** 2 + kenar2 ** 2 = hipotenus**2
            if (self.kenar1)**2 + (self.kenar2)**2 == self.hipotenus**2:
                print("Bu üçgen bir dik üçgendir.")
                print(f"Kenar 1 : {self.kenar1} Kenar 2 : {self.kenar2} Hipotenüs : {self.hipotenus}")
            else:
                print("Bu üçgen bir çeşitkenar üçgendir.")


    def hipotenusuBul(self):

        if self.kenar1 > self.kenar2 and self.kenar1 > self.hipotenus:
            temp = self.hipotenus
            self.hipotenus = self.kenar1
            self.kenar1 = temp
        elif self.kenar2 > self.kenar1 and self.kenar2 > self.hipotenus:
            temp = self.hipotenus
            self.hipotenus = self.kenar2
            self.kenar2 = temp

    def ucgenMiDegilMi(self , kenar1 , kenar2 , hipotenus):

        if kenar1+kenar2 < hipotenus:
            return False
        elif kenar1+hipotenus < kenar2:
            return False
        elif hipotenus+kenar2 < kenar1:
            return False
        return True


ucgen = Ucgen(3.087069808086626 , 1.3 , 2.8)