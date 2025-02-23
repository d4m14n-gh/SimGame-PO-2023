from roslina import Roslina
from organizm import WynikKolizji, Organizm


class Guarana(Roslina):
    def __init__(self):
        super().__init__(0)

    def kolizja(self, atakujacy):
        atakujacy.sila = atakujacy.sila + 3
        return WynikKolizji.wygrana

    def get_symbol(self):
        return 'G'

    def get_kolor(self):
        return Organizm.gradient("#B61D1D", "#831717", self.wiek, 100)
