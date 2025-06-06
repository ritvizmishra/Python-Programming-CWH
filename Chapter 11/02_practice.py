class Animals:
    def __init__(self, types):
        self.types = types

class Pets(Animals):
    def __init__(self, types, species):
        super().__init__(types)
        self.species = species

class Dogs(Pets):
    def __init__(self, types, species, breeds):
        super().__init__(types, species)
        self.breeds = breeds
    
    def show(self):
        print(f"The animal you've chosen is {self.types}.\nIt belongs to class {self.species}.\nAnd, is a {self.breeds}.")
    
    @staticmethod
    def bark():
        print("\ni'm barking :)")

an = Dogs("omnivores", "dog", "beagle")
an.show()
an.bark()