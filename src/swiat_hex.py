from swiat import Swiat
from punkt import Punkt


class SwiatHex(Swiat):
    def __init__(self, w, h):
        super().__init__(w, h)

    def znajdz_sasiadow(self, pozycja: Punkt, promien: int = 1):
        mozliwe_pozycje = []
        if promien > 1:
            for p in self.znajdz_sasiadow(pozycja, promien - 1):
                for p2 in self.znajdz_sasiadow(p, 1):
                    if p2 != pozycja and (p2 not in mozliwe_pozycje):
                        mozliwe_pozycje.append(p2)
            return mozliwe_pozycje
        for x in range(-promien + (pozycja.y % 2), promien - ((pozycja.y + 1) % 2) + 1):
            for y in range(-promien, promien + 1):
                mozliwa_pozycja = Punkt(pozycja.x + x, pozycja.y + y)
                if self.na_mapie(mozliwa_pozycja) and mozliwa_pozycja != pozycja:
                    mozliwe_pozycje.append(mozliwa_pozycja)
        if pozycja.y % 2 == 1 and self.na_mapie(Punkt(pozycja.x - 1, pozycja.y)):
            mozliwe_pozycje.append(Punkt(pozycja.x - 1, pozycja.y))
        if pozycja.y % 2 == 0 and self.na_mapie(Punkt(pozycja.x + 1, pozycja.y)):
            mozliwe_pozycje.append(Punkt(pozycja.x + 1, pozycja.y))
        return mozliwe_pozycje

    @staticmethod
    def is_hex():
        return True
