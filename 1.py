import os 
os.system("cls")


class Mahsulotlar:
    def __init__(self,nom,narx,miqdor):
        self.nom=nom
        self.narx=narx
        self.miqdor=miqdor

    def sotib_ol(self,miqdor):
        self.miqdor-=miqdor
    
    def qolgan_miqdor(self):
        return self.miqdor

olma=Mahsulotlar("Olma",20000,10)


olma.sotib_ol(2)
olma.sotib_ol(3)

print(f"Qolgan miqdor:{olma.qolgan_miqdor()}")