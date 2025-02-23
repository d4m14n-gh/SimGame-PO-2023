from czlowiek import Czlowiek
from organizm import Organizm
from punkt import Punkt
import pickle


class Swiat:
    def __init__(self, szerokosc: int, wysokosc: int):
        self._wysokosc = wysokosc
        self._szerokosc = szerokosc
        self._tura = 0
        self._organizmy = {}
        self._czlowiek = None
        self._wp = None

    def na_mapie(self, punkt: Punkt):
        return not (punkt.x < 0 or punkt.y < 0 or punkt.x >= self._szerokosc or punkt.y >= self._wysokosc)

    def dodaj_organizm(self, organizm: Organizm, pozycja: Punkt, komunikat: bool = False):
        if not self.na_mapie(pozycja):
            return
        if isinstance(organizm, Czlowiek):
            if self._czlowiek:
                return
            else:
                self._czlowiek = organizm
        if komunikat:
            # print(f"Dodano {organizm} na {pozycja}")
            self.wypisz(f"Dodano {organizm} na {pozycja}")
        self._organizmy[pozycja] = organizm
        organizm.pozycja = pozycja
        organizm.swiat = self

    def znajdz_organizm(self, pozycja: Punkt):
        if pozycja in self._organizmy:
            return self._organizmy[pozycja]
        else:
            return None

    def usun_organizm(self, pozycja: Punkt, komunikat: bool = False):
        if pozycja in self._organizmy:
            if komunikat:
                # print(f"Usunieto {self.organizmy[pozycja]} z {pozycja}")
                self.wypisz(f"Usunieto {self._organizmy[pozycja]} z {pozycja}")
            if isinstance(self._organizmy[pozycja], Czlowiek):
                self._czlowiek = None
            self._organizmy.pop(pozycja)

    def przesun_organizm(self, stara_pozycja: Punkt, nowa_pozycja: Punkt):
        self.usun_organizm(nowa_pozycja)
        self._organizmy[nowa_pozycja] = self._organizmy[stara_pozycja]
        self._organizmy.pop(stara_pozycja)

    def wykonaj_ture(self):
        self._tura += 1
        # print(f"\nPoczatek tury {self.tura}:")
        self.wypisz(f"\nPoczatek tury {self._tura}:")
        organizmy = []
        for y in range(0, self._wysokosc):
            for x in range(0, self._szerokosc):
                if Punkt(x, y) in self._organizmy:
                    organizmy.append(self._organizmy[Punkt(x, y)])
        organizmy.sort(key=lambda o: o.get_inicjatywa()*10000+o.wiek, reverse=True)
        for organizm in organizmy:
            if organizm.pozycja not in self._organizmy:
                continue
            if organizm != self._organizmy[organizm.pozycja]:
                continue
            organizm.akcja()
            organizm.wiek += 1

    def znajdz_sasiadow(self, pozycja: Punkt, promien: int = 1):
        mozliwe_pozycje = []
        for x in range(-promien, promien + 1):
            for y in range(-promien, promien + 1):
                mozliwa_pozycja = Punkt(pozycja.x + x, pozycja.y + y)
                if self.na_mapie(mozliwa_pozycja) and mozliwa_pozycja != pozycja:
                    mozliwe_pozycje.append(mozliwa_pozycja)
        return mozliwe_pozycje

    def wypisz(self, tekst: str):
        if self._wp:
            self._wp(tekst)

    def rysuj(self):
        print(f'swiat tura: {self._tura} o wymiarach w:{self._szerokosc} h:{self._wysokosc}')
        for y in range(self._wysokosc - 1, -1, -1):
            for x in range(0, self._szerokosc):
                if Punkt(x, y) in self._organizmy:
                    print(" " + self._organizmy[Punkt(x, y)].get_symbol(), end="")
                else:
                    print(" \033[92m.", end="\033[97m")
            print()

    def zapisz(self, slot: int):
        nazwa = f"saves/{self.__class__.__name__}{slot}-{self._szerokosc}x{self._wysokosc}.sv"
        wp = self._wp
        with open(nazwa, "wb") as file:
            # print("\n>Zapisano stan swiata: "+nazwa)
            self.wypisz("\n>Zapisano stan swiata: "+nazwa)
            self._wp = None
            pickle.dump((self, self._organizmy), file)
        self._wp = wp

    def wczytaj(self, slot: int):
        try:
            nazwa = f"saves/{self.__class__.__name__}{slot}-{self._szerokosc}x{self._wysokosc}.sv"
            with open(nazwa, "rb") as file:
                # print("\n<Wczytano stan swiata: "+nazwa)
                self.wypisz("\n<Wczytano stan swiata: "+nazwa)
                d = pickle.load(file)
                self._tura = d[0].get_tura()
                self._czlowiek = d[0].get_czlowiek()
                self._organizmy = d[1]
                for punkt in self._organizmy:
                    self._organizmy[punkt].swiat = self

        except FileNotFoundError:
            # print("\n!Nie można wczytać save'a.")
            self.wypisz("\n!Nie można wczytać save'a.")

    def set_konsola(self, konsola):
        self._wp = konsola

    def get_wysokosc(self):
        return self._wysokosc

    def get_szerokosc(self):
        return self._szerokosc

    def get_tura(self):
        return self._tura

    def get_czlowiek(self):
        return self._czlowiek

    def get_organizmy(self):
        return self._organizmy

    @staticmethod
    def is_hex():
        return False
