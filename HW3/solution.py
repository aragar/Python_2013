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

    # some parent may be missing;
    # self could be in the list;
    def get_brothers(self):
        return list(set(self.mother.children('M') + self.father.children('M')))

    # some parent may be missing;
    # self could be in the list;
    def get_sisters(self):
        return list(set(self.mother.children('F') + self.father.children('F')))

    def children(self, gender=None):
        if gender:
            return [child for child in self._children if child.gender == gender]
        else:
            return self._children

    def is_direct_successor(self, person):
        return (self.mother == person or self.father == person or 
        	self == person.mother or self == person.father)
