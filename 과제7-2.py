class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def death(self):
        Doggy.num_of_dogs -= 1
        print(f'{self.name} is dead')

    @classmethod
    def get_status(cls):
        print(f'birth_of_dogs:{cls.birth_of_dogs}, num_of_dogs:{cls.num_of_dogs}')

    def bark(self):
        print('왈왈')

dog_1 = Doggy('popo', 'poodle')
dog_2 = Doggy('dada','maltese')
print(dog_1.name)
print(dog_1.species)
dog_1.bark()
dog_2.death()
Doggy.get_status()
