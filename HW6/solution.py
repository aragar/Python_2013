from itertools import accumulate, repeat


class IndexError(Exception):
    pass


class ValueError(Exception):
    pass


class TypeError(Exception):
    pass


class Death(Exception):

    pass


class Vec2D:

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

    def __iter__(self):
        return iter((self.x, self.y))


class World:

    def __init__(self, width):
        self._width = width
        self._world = [CellRow(width) for _ in range(width)]

    def __len__(self):
        return self._width

    def __getitem__(self, key):
        if key < 0 or key >= self._width:
            raise IndexError

        return self._world[key]


class Cell:

    def __init__(self, contents=None):
        self.contents = contents

    def is_empty(self):
        return self.contents is None

    def __setattr__(self, name, value):
        if name == 'contents' and value is not None and \
                not isinstance(value, WorldObject):
            raise TypeError
        else:
            super().__setattr__(name, value)


class CellRow:

    def __init__(self, width):
        self._row = [Cell() for _ in range(width)]

    def __getitem__(self, key):
        if key < 0 or key >= len(self._row):
            raise IndexError

        return self._row[key]

    def __setitem__(self, key, value):
        if key < 0 or key >= len(self._row):
            raise IndexError

        self._row[key].contents = value


class WorldObject:

    pass


class Food(WorldObject):

    def __init__(self, energy=0):
        self.energy = energy


class PythonPart(WorldObject):

    def __init__(self, direction=Vec2D()):
        self._direction = direction


class PythonHead(PythonPart):

    def __init__(self, coords=Vec2D()):
        self._coords = coords


class Python:
    LEFT = Vec2D(-1, 0)
    UP = Vec2D(0, 1)
    RIGHT = Vec2D(1, 0)
    DOWN = Vec2D(0, -1)
    OPPOSITE = {LEFT: RIGHT, UP: DOWN, RIGHT: LEFT, DOWN: UP}

    def __init__(self, world, coords, size, direction):
        self._world = world

        self.size = size
        self.direction = direction

        self._head = PythonHead(coords)
        self._body = [PythonPart(self.OPPOSITE[direction])
                      for _ in range(size)]

        world[coords.x][coords.y].contents = self._head
        for i, offset in enumerate(accumulate(repeat(self.OPPOSITE[direction], size))):
            world[coords.x + offset.x][coords.y + offset.y] = self._body[i]

    def move(self, direction):
        pass
