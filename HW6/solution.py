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
    def __init__(self):
        print("A cell is made")


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
    pass


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
    pass


class Death(Exception):

    """ The Death itself. """
    pass
