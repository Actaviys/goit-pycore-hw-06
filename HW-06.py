from collections import UserDict


class Field:#Батьківський клас
    def __init__(self, value):
        self.nicname = value
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
class Name(Field):
    pass

class Phone(Field):
    pass

class Record:
    def __str__(self):
        return f"'name': ''"
    
val = Field("fe.er \nqw")
 
print(val.value)