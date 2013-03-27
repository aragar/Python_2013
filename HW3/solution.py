class Person:

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.birth_year = kwargs['birth_year']
        self.gender = kwargs['gender']

        self.father = kwargs.get('father', None)
        self.mother = kwargs.get('mother', None)

    def get_brothers(self):
        pass

    def get_sisters(self):
        pass

    def children(self, gender=None):
        pass

    def is_direct_successor(self, person):
    	pass