class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner= None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.add_pet_to_all()

    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, type_of_pet):
        if type_of_pet in Pet.PET_TYPES:
            self._pet_type = type_of_pet
        else : 
            raise ValueError("Pet type not in list of valid pet types.")
        
    def add_pet_to_all(self):
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instanc eof the Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(Pet.all, key = lambda pet: pet.name)