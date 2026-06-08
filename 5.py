import math
import os
os.system("cls")

class Uchburchak:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self):
        return self.a + self.b + self.c

    def maydon(self):
        s = self.perimetr() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


uch = Uchburchak(3, 4, 5)
print(f"Perimetr: {uch.perimetr()}")
print(f"Maydon: {uch.maydon()}")



