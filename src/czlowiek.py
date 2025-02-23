from organizm import WynikKolizji, Organizm
from zwierze import Zwierze
from punkt import Punkt
from random import choice


class Czlowiek(Zwierze):
    def __init__(self):
        super().__init__(5, 4)
        self.kierunek = Punkt(0, 0)
        self._umiejetnosc = 0

    def kolizja(self, atakujacy: Organizm):
        if self._umiejetnosc <= 0:
            return super().kolizja(atakujacy)
        mozliwe_pozycje = []
        for pozycja in self.swiat.znajdz_sasiadow(self.pozycja):
            if not self.swiat.znajdz_organizm(pozycja):
                mozliwe_pozycje.append(pozycja)
        # print(f"{atakujacy} trafia na tarcze alzura na {self.pozycja}")
        self.swiat.wypisz(f"{atakujacy} trafia na tarcze alzura na {self.pozycja}")
        if mozliwe_pozycje:
            nowa_pozycja = choice(mozliwe_pozycje)
            atakujacy.pozycja = nowa_pozycja
        return WynikKolizji.wycofanie

    def aktywuj_umiejetnosc(self):
        if self._umiejetnosc > 0:
            # print(f"{self} z {self.pozycja} przedluza tarcze Alzura")
            self.swiat.wypisz(f"{self} z {self.pozycja} przedluza tarcze Alzura")
        else:
            # print(f"{self} z {self.pozycja} aktywuje tarcze Alzura")
            self.swiat.wypisz(f"{self} z {self.pozycja} aktywuje tarcze Alzura")
        self._umiejetnosc = 5

    def akcja(self):
        self._umiejetnosc -= 1
        nowa_pozycja = self.pozycja + self.kierunek
        if self.swiat.na_mapie(nowa_pozycja) and nowa_pozycja != self.pozycja:
            self._ruch([self.pozycja+self.kierunek])

    def rozmnoz(self):
        return False

    def get_kolor(self):
        if self._umiejetnosc > 0:
            return "#89A29E"
        else:
            return "#C7AE98"

    def get_symbol(self):
        return 'H'

    def set_kierunek(self, value):
        self.kierunek = value
