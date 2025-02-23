from random import choice
from organizm import Organizm, WynikKolizji
from zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self):
        super().__init__(4, 7)

    def akcja(self):
        mozliwe_pozycje = self.swiat.znajdz_sasiadow(self.pozycja, 2)
        self._ruch(mozliwe_pozycje)

    def kolizja(self, atakujacy: Organizm):
        if isinstance(atakujacy, self.__class__):
            return WynikKolizji.rozmnazanie
        elif self.sila > atakujacy.sila:
            return WynikKolizji.porazka
        else:
            mozliwe_pozycje = self.swiat.znajdz_sasiadow(self.pozycja, 1)
            pozycje_do_usuniecia = []
            for pozycja in mozliwe_pozycje:
                if self.swiat.znajdz_organizm(pozycja):
                    pozycje_do_usuniecia.append(pozycja)
            for pozycja in pozycje_do_usuniecia:
                mozliwe_pozycje.remove(pozycja)
            if mozliwe_pozycje and choice([True, False]):
                nowa_pozycja = choice(mozliwe_pozycje)
                self.swiat.przesun_organizm(self.pozycja, nowa_pozycja)
                # print(f"{str(self)} z {self.pozycja}: uczieczka przed {str(atakujacy)} na {nowa_pozycja}")
                self.swiat.wypisz(f"{str(self)} z {self.pozycja}: uczieczka przed {str(atakujacy)} na {nowa_pozycja}")
                self.pozycja = nowa_pozycja
            return WynikKolizji.wygrana

    def get_symbol(self):
        return 'A'

    def get_kolor(self):
        return "#813A12"

