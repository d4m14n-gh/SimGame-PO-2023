from random import randint
from organizm import Organizm
import abc


class Roslina(Organizm, abc.ABC):
    def __init__(self, sila):
        super().__init__(sila, 0)

    def akcja(self):
        self.rozmnoz()

    def rozmnoz(self):
        if randint(0, 14) == 0:
            return super().rozmnoz()
        return True
