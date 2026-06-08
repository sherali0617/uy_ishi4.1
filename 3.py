import os
os.system("cls")

class Avtomobil:
    def __init__(self,model,yil,tezlik):
        self.model=model
        self.yil=yil
        self.tezlik=tezlik

    def tezlashtir(self):
        self.tezlik+=10
        

    def sekinlashtir(self):
        self.tezlik-=10
    
    def info(self):
        print(f"Model:{self.model},yil:{self.yil},tezlik:{self.tezlik}")


car=Avtomobil("Tahoe",2025,0)
car.tezlashtir()
car.tezlashtir()
car.tezlashtir()

# 1 marta sekinlashtirish
car.sekinlashtir()

car.info()
 

    