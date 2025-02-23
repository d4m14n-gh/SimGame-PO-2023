from random import choice
from zwierze import Zwierze
from organizm import Organizm, WynikKolizji


class Zolw(Zwierze):
    def __init__(self):
        super().__init__(2, 1)

    def akcja(self):
        if choice(range(0, 4)) == 0:
            super().akcja()

    def kolizja(self, atakujacy: Organizm):
        if isinstance(atakujacy, self.__class__):
            return WynikKolizji.rozmnazanie
        elif self.sila > atakujacy.sila:
            return WynikKolizji.porazka
        elif atakujacy.sila < 5:
            # print(f"{str(self)} z {self.pozycja}: odstrasza {str(atakujacy)}")
            self.swiat.wypisz(f"{str(self)} z {self.pozycja}: odstrasza {str(atakujacy)}")
            return WynikKolizji.wycofanie
        else:
            return WynikKolizji.wygrana

    def get_symbol(self):
        return 'Z'

    def get_kolor(self):
        return "#9F9357"



