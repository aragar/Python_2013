from itertools import accumulate, repeat


class IndexError(Exception):
    pass


class ValueError(Exception):
    pass


class Death(Exception):

    """ The Death itself. """
    pass


class Vec2D:

    """ A 2D vector. """
    def __init__(self, x=0, y=0):
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

    def __setitem__(self, key, value):
        if key < 0 or key >= self._width:
            raise IndexError

        self._row[key].contents = value


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
    def __init__(self, direction=Vec2D()):
        self._direction = direction


class PythonHead(PythonPart):

    """ The python's head. """
    def __init__(self, coords=Vec2D()):
        self._coords = coords


class Python:
    LEFT = Vec2D(-1, 0)
    UP = Vec2D(0, 1)
    RIGHT = Vec2D(1, 0)
    DOWN = Vec2D(0, -1)
    OPPOSITE = {LEFT: RIGHT, UP: DOWN, RIGHT: LEFT, DOWN: UP}

    """ This is the class modelling the python itself. """
    def __init__(self, world, coords, size, direction):
        self._world = world
        self.size = size
        self._head = PythonHead(coords, direction)
        self._body = [PythonPart(self.OPPOSITE[direction])
                      for _ in range(size)]

    def move(self, direction):
        pass
