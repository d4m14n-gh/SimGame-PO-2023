from punkt import Punkt
from enum import Enum
from random import choice
import abc


class Organizm(abc.ABC):
    def __init__(self, sila: int, inicijatywa: int):
        self.sila = sila
        self.wiek = 0
        self._inicijatywa = inicijatywa
        self.pozycja = Punkt(0, 0)
        self.swiat = None

    def akcja(self):
        pass

    def kolizja(self, atakujacy):
        if isinstance(atakujacy, self.__class__):
            return WynikKolizji.rozmnazanie
        elif self.sila > atakujacy.sila:
            return WynikKolizji.porazka
        else:
            return WynikKolizji.wygrana

    def stworz_nowy(self):
        nowy = self.__class__()
        nowy.sila = (nowy.sila + self.sila) // 2
        return nowy

    def rozmnoz(self):
        mozliwe_pozycje = self.swiat.znajdz_sasiadow(self.pozycja)
        pozycje_do_usuniecia = []
        for pozycja in mozliwe_pozycje:
            if self.swiat.znajdz_organizm(pozycja):
                pozycje_do_usuniecia.append(pozycja)
        for pozycja in pozycje_do_usuniecia:
            mozliwe_pozycje.remove(pozycja)
        if not mozliwe_pozycje:
            return False
        nowa_pozycja = choice(mozliwe_pozycje)
        self.swiat.dodaj_organizm(self.stworz_nowy(), nowa_pozycja)
        return True

    @staticmethod
    def gradient(p, q, wiek: int, maks_wiek: int):
        return p
        p_red = int(p[1:3], 16)
        p_green = int(p[3:5], 16)
        p_blue = int(p[5:7], 16)
        q_red = int(q[1:3], 16)
        q_green = int(q[3:5], 16)
        q_blue = int(q[5:7], 16)
        dr = q_red - p_red
        dg = q_green - p_green
        db = q_blue - p_blue
        mltp = min(wiek / float(maks_wiek), 1.0)
        c = 10
        red = p_red + (int(dr * mltp) // c) * c
        green = p_green + (int(dg * mltp) // c) * c
        blue = p_blue + (int(db * mltp) // c) * c
        return f"#{red:02x}{green:02x}{blue:02x}"

    @staticmethod
    def avg_color(kolor):
        red = int(kolor[1:3], 16)
        green = int(kolor[3:5], 16)
        blue = int(kolor[5:7], 16)
        avg = (red + green + blue) // 3
        return avg

    def get_symbol(self):
        pass

    def get_kolor(self):
        return "black"

    def __str__(self):
        return self.__class__.__name__

    def get_inicjatywa(self):
        return self._inicijatywa


class WynikKolizji(Enum):
    wygrana = 1
    porazka = 2
    wycofanie = 3
    rozmnazanie = 4
