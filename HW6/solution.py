class IndexError(Exception):
    pass


class World:

    """ The world of the pythons. """

    def __init__(self, width):
        this._width = width
        this._world = [CellRow(width) for _ in range(width)]

    def __len__(self):
        return self._width

    def __getitem__(self, key):
        if key < 0 or key >= self._width:
            raise IndexError

        return self._world[key]


class Cell:

    """ A cell in the world of the pythons. """
    def __init__(self, contents=None):
        self.contents = contents

    def is_empty(self):
        return self.contents is None


class CellRow:

    """ Implementation of a row of Cells. """
    def __init__(self, width):
        self._row = [Cell() for _ in range(width)]

    def __getitem__(self, key):
        if key < 0 or key >= len(self._row):
            raise IndexError

        return self._row[key]


class WorldObject:

    """ Object in the pythons' world. Every object in this world should inherit
    this class.

    """
    pass


class Food(WorldObject):

    """ Some food. """
    def __init__(self, energy=0):
        self.energy = energy


class PythonPart(WorldObject):

    """ The parts of a python. """
    pass


class PythonHead(PythonPart):

    """ The python's head. """
    pass


class Python:

    """ This is the class modelling the python itself. """
    pass


class Vec2D:

    """ A 2D vector. """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return Vec2D(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self * other

    def __iadd__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def __isub__(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

    def __imul__(self, other):
        self.x = self.x * other
        self.y = self.y * other

    def __neg__(self):
        return Vec2D(-self.x, -self.y)



class Death(Exception):

    """ The Death itself. """
    pass
