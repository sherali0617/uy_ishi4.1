class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif


class Kutubxona:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def qidirish(self, nom):
        for kitob in self.kitoblar:
            if kitob.nomi.lower() == nom.lower():
                return f"Topildi: {kitob.nomi} - {kitob.muallif}"
        return "Kitob topilmadi!"



kutubxona = Kutubxona()


kutubxona.kitob_qoshish(Kitob("O'tkan Kunlar", "Abdulla Qodiriy"))
kutubxona.kitob_qoshish(Kitob("Mehrobdan Chayon", "Abdulla Qodiriy"))
kutubxona.kitob_qoshish(Kitob("Sarob", "Abdulla Qahhor"))
kutubxona.kitob_qoshish(Kitob("Shum Bola", "G'afur G'ulom"))


print(kutubxona.qidirish("Sarob"))
print(kutubxona.qidirish("Alvido"))