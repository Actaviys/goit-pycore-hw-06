
from collections import UserDict


""" 
{
    'fish': [...],
    'lion': [...]
}
"""

class Mammal:
    def Walk(self):
        print("Walking")
        
class Fish:
    def swim(self):
        print("Swiming")

class Dolphin(Fish):
    def walk(self):
        raise TypeError

class Lion(Mammal):
    pass

class Duck(Mammal, Fish):
    pass


class Zoo(UserDict):
    
    def animal_put(self, enclose_name: str, animal):
        if enclose_name in self:
            self[enclose_name].append(animal)
        else:
            self[enclose_name] = [animal]
            
            
    
    
    def add_animal(self, animal):
        match animal:
            case Lion():
                print("Add Lion")
            case Mammal():
                print("Add Mammal")
            case Dolphin():
                print("Add Dolphin")
            case _:
                print("Add General")
    





zoo = Zoo()
print(zoo)

zoo.animal_put("fish", Fish)
# zoo.animal_put("fish", Fish)
print(zoo)








# class Zoo(UserDict):
#     # def __init__(self) -> Noneone:
#     #     super().__init__
    
#     def add_animal(self, animal):
#         # self.data['fish'].append(animal)
#         # self['fish'].append(animal)
#         if type(animal) == Fish:
#             pass
#         elif type(animal) == Lion:
#             pass
#         elif type(animal) == Duck:
#             pass
        #    if isinstance(animal, Duck) 
    