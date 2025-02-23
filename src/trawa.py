from roslina import Roslina


class Trawa(Roslina):
    def __init__(self):
        super().__init__(1)

    def get_symbol(self):
        return 'T'

    def get_kolor(self):
        return self.gradient("#3EBB45", "#489B54", self.wiek, 150)



