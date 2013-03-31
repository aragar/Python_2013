class Person:

    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender

        self.mother = mother
        self.father = father

        self._children = list()

        for parent in [mother, father]:
            if parent:
                parent._add_child(self)

    def _add_child(self, child):
        self._children.append(child)

    def __get_known_parents(self):
        return [parent for parent in [self.mother, self.father] if
                parent is not None]

    def __get_siblings(self, gender):
    	siblings = set()
    	for parent in self.__get_known_parents():
    		siblings |= set(parent.children(gender))
    	siblings -= {self}
    	return siblings

    def get_brothers(self):
        return list(self.__get_siblings('M'))

    def get_sisters(self):
    	return list(self.__get_siblings('F'))

    def children(self, gender=None):
        if gender:
            return [child for child in self._children if child.gender == gender]
        else:
            return self._children

    def is_direct_successor(self, person):
        return person.mother == self or person.father == self
