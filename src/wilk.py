from zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self):
        super().__init__(9, 5)

    def get_symbol(self):
        return 'W'

    def get_kolor(self):
        return "#707070"

