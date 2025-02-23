class Punkt:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punkt(self.x+other.x, self.y+other.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        return not (self == other)

    def __copy__(self):
        return Punkt(self.x, self.y)

    def __str__(self):
        return "{" + str(self.x) + ";" + str(self.y) + "}"

    def __hash__(self):
        return self.x*10000+self.y
