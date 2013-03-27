class Person:

    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender

        sef.mother = mother
        self.father = father

        self._children = list()

        for parent in [mother, father]:
            if parent:
                parent._add_child(self)

    def _add_child(self, child):
        self.children.append(child)

    def get_brothers(self):
        return self.mother.children('M') + self.father.children('M')

    def get_sisters(self):
        return self.mother.children('F') + self.father.children('F')

    def children(self, gender=None):
        if gender:
            return [child for child in self.children if child.gender == gender]
        else:
            return self.children

    def is_direct_successor(self, person):
        return self.mother == person or self.father == person
