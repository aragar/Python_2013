class IndexError(Exception):
    pass


class World:

    """ The world of the pythons. """

	def __init__(self, width):
		this.width = width

	def __len__(self):
		return self.width



class Cell:

    """ A cell in the world of the pythons. """
    pass


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
