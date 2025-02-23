from random import random
from roslina import Roslina
from zwierze import Zwierze


class BarszczSosnowskiego(Roslina):
    def __init__(self):
        super().__init__(10)

    def akcja(self):
        if random() < 0.2:
            super().akcja()
        pozycje = self.swiat.znajdz_sasiadow(self.pozycja)
        for pozycja in pozycje:
            if pozycja in self.swiat._organizmy:
                organizm = self.swiat.znajdz_organizm(pozycja)
                if isinstance(organizm, Zwierze) and str(organizm) != "Cyber owca":
                    self.swiat.usun_organizm(pozycja)

    def get_symbol(self):
        return 'B'

    def get_kolor(self):
        return self.gradient("#76A97B", "#4A645D", self.wiek, 100)

    def __str__(self):
        return "Barszcz sosnowskiego"
