from collections import deque
from zwierze import Zwierze
from punkt import Punkt
from barszcz_sosnowskiego import BarszczSosnowskiego


class CyberOwca(Zwierze):
    barszcz = True

    def __init__(self):
        super().__init__(11, 4)

    def akcja(self):
        odleglosci = {}
        q = deque()
        q.append(self.pozycja)
        odleglosci[self.pozycja] = 0
        cel = None
        while q:
            t = q.popleft()
            if t in self.swiat._organizmy and isinstance(self.swiat._organizmy[t], BarszczSosnowskiego):
                cel = t
                break
            for p in self.swiat.znajdz_sasiadow(t):
                if p not in odleglosci:
                    odleglosci[p] = odleglosci[t] + 1
                    q.append(p)
        if not cel:
            self.barszcz = False
            super().akcja()
            return
        self.barszcz = True

        nextp = cel
        while True:
            if odleglosci[nextp] == 1:
                break
            for p in self.swiat.znajdz_sasiadow(nextp):
                if p in odleglosci and odleglosci[p] == odleglosci[nextp] - 1:
                    nextp = p
                    break

        mozliwe_pozycje = [nextp]
        self._ruch(mozliwe_pozycje)

    def get_symbol(self):
        return 'C'

    def get_kolor(self):
        # if self.barszcz:
        return "#24b8ab"
        # else:
        return "#DBD8CF"

    def __str__(self):
        return "Cyber owca"
