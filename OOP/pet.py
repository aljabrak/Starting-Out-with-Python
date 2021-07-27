# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 568.
# Q. 1 Pet Class.


class Pet:
    def __init__(self, animal_name, animal_type, animal_age):
        self.__name  = animal_name
        self.__animal_type = animal_type
        self.__age = animal_age
    
    def set_name(self, animal_name):
        self.__name  = animal_name
        
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    def set_age(self, animal_age):
        self.__age = animal_age
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age

def main():
    name = input("Animal Name: ")
    animal_type = input("Animal Type: ")
    age = str(input("Animal Age: "))

    pet = Pet(name, animal_type, age)
    print("\n")
    print("Animal name is: ", pet.get_name())
    print("Animal type is: ", pet.set_animal_type(animal_type))
    print("Animal age is: ", pet.get_age())

main()
