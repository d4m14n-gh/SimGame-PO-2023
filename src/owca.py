from zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self):
        super().__init__(4, 4)

    def get_symbol(self):
        return 'O'

    def get_kolor(self):
        return "#DAD8CF"

