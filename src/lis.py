from zwierze import Zwierze
from organizm import Organizm, WynikKolizji
from random import choice


class Lis(Zwierze):
    def __init__(self):
        super().__init__(3, 7)

    def akcja(self):
        mozliwe_pozycje = self.swiat.znajdz_sasiadow(self.pozycja)
        pozycje_do_usuniecia = []
        for pozycja in mozliwe_pozycje:
            if self.swiat.znajdz_organizm(pozycja) and self.swiat.znajdz_organizm(pozycja).sila > self.sila:
                pozycje_do_usuniecia.append(pozycja)
        for pozycja in pozycje_do_usuniecia:
            mozliwe_pozycje.remove(pozycja)
        self._ruch(mozliwe_pozycje)

    def get_symbol(self):
        return 'L'

    def get_kolor(self):
        return "#CE6110"
