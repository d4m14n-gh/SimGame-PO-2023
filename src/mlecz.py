from roslina import Roslina


class Mlecz(Roslina):
    def __init__(self):
        super().__init__(0)

    def akcja(self):
        for _ in range(3):
            self.rozmnoz()

    def get_symbol(self):
        return 'M'

    def get_kolor(self):
        return self.gradient("#FFE00C", "#B6B6A9", self.wiek, 150)

