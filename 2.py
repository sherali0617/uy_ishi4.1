import os
os.system("cls")

class Kitob:
    def __init__(self,nomi,muallifi,sahifa_soni):
        self.nomi=nomi
        self.muallifi=muallifi
        self.sahifa_soni=sahifa_soni

    def qisqacha(self):
        return f"{self.nomi}-{self.muallifi},{self.sahifa_soni} sahifa"
    
    def katta_kitobmi(self):
        return self.sahifa_soni>300
    
kitob1=Kitob("Mehrobdan chayon","Abdulla Qodiriy",450)
kitob2 = Kitob("O'tkan Kunlar", "Abdulla Qodiriy", 520)
kitob3 = Kitob("Sarob", "Abdulla Qahhor", 180)
kitob4 = Kitob("Shum Bola", "G'afur G'ulom", 95)

kitoblar=[kitob1,kitob2,kitob3,kitob4]

for i in kitoblar:
    print(i.qisqacha(),"Katta kitob:",i.katta_kitobmi())

