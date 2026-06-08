import os
os.system("cls")

class BankHisob:
    def __init__(self,ism,balans=0):
        self.ism=ism
        self.balans=balans
    def deposit(self,summa):
        self.balans+=summa
        print(f"{summa} so'm qo'shildi!")
    def yechib_ol(self,summa):
        if self.balans>=summa:
            self.balans-=summa
            print(f"{summa} so'm yechib olindi!")
        else:
            print("balans yetarli emas!")
    def hisob(self):
        return self.balans

ali = BankHisob("Ali")

ali.deposit(1000)
ali.yechib_ol(400)

print(f"Joriy balans: {ali.hisob()} so'm")