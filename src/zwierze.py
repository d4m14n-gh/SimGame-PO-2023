from random import choice
from organizm import Organizm, WynikKolizji
from punkt import Punkt
from typing import List
import abc


class Zwierze(Organizm, abc.ABC):
    def __init__(self, sila, inicjatywa):
        super().__init__(sila, inicjatywa)

    def _ruch(self, mozliwe_pozycje: List[Punkt]):
        if not mozliwe_pozycje:
            return
        nowa_pozycja = choice(mozliwe_pozycje)
        obecny = self.swiat.znajdz_organizm(nowa_pozycja)
        if obecny:
            wynik_kolizji = obecny.kolizja(self)
            wynik = str(wynik_kolizji).removeprefix("WynikKolizji.")
            if wynik_kolizji == WynikKolizji.porazka:
                # print(f"{str(self)} z {self.pozycja}: {wynik} z {str(obecny)} na {nowa_pozycja}")
                self.swiat.wypisz(f"{str(self)} z {self.pozycja}: {wynik} z {str(obecny)} na {nowa_pozycja}")
                self.swiat.usun_organizm(self.pozycja)
                return
            if wynik_kolizji == WynikKolizji.wycofanie:
                return
            if wynik_kolizji == WynikKolizji.rozmnazanie:
                obecny.rozmnoz()
                return
            # print(f"{str(self)} z {self.pozycja}: {wynik} z {str(obecny)} na {nowa_pozycja}")
            self.swiat.wypisz(f"{str(self)} z {self.pozycja}: {wynik} z {str(obecny)} na {nowa_pozycja}")
        self.swiat.przesun_organizm(self.pozycja, nowa_pozycja)
        self.pozycja = nowa_pozycja

    def akcja(self):
        mozliwe_pozycje = self.swiat.znajdz_sasiadow(self.pozycja)
        self._ruch(mozliwe_pozycje)

    def get_symbol(self):
        pass
