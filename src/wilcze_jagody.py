from roslina import Roslina
from organizm import Organizm, WynikKolizji


class WilczeJagody(Roslina):
    def __init__(self):
        super().__init__(99)

    def kolizja(self, atakujacy):
        if atakujacy.sila >= self.sila:
            return WynikKolizji.wygrana
        self.swiat.usun_organizm(self.pozycja)
        return WynikKolizji.porazka

    def get_symbol(self):
        return 'J'

    def get_kolor(self):
        return self.gradient("#7B45D2", "#490F7A", self.wiek, 20)

    def __str__(self):
        return "Wilcze jagody"
