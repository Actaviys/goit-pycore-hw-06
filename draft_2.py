


from collections import UserDict
from collections.abc import Iterable


class AddressBook(UserDict):
    def add_record(self, value):
        self.data = value
    # def add_record(self, key, value):
        # self.data[key] = value    
    


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
        
class Name(Field):
    def __init__(self, name) -> None:
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone) -> None:
        super().__init__(phone)
    



class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.res = {"Katya": 23423}
        
        
    def add_phone(self, phon):
        self.phones.append(phon)
    
    
    # def __str__(self):
    #     r = f"{self.name}: {self.phones}"
    #     self.res.update({self.name : self.phones})
    #     return self.res
    # # def __getstate__(self) -> object:
    # #     return self.res
        
    
    
    
    
        
        
        
    


###
# # Створення нової адресної книги
book = AddressBook()#Створюю адресну книгу
# pho = [23423,1111111]
# nam = "Lisa"
# book.add_record(nam, pho) #№1 Записую по-> ключ:значення
# book.add_record("Lyda", 23423) #№2 Записую по-> ключ:значення
# lisa_r = {"lisa": 33333}
# book.add_record(lisa_r) #№ 3 Записую по-> ключ:значення
# print(f"AdresBook -> {book}")#Виводжу резльтат списку


# Створення запису для John
john_r = Record("John")
john_r.add_phone("1234567890")
john_r.add_phone("5555555555")

# # Додавання запису John до адресної книги
book.add_record(john_r)
print(f"Record -> {john_r}") 
print(f"AdresBook -> {book}")#Виводжу резльтат списку



# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
###




# pho = [23423,1111111]
# nam = "Lisa"
# user = Record(name=nam)
# print(user.name)
# # print(data)


# na = "Dima"
# ph = [23423,1111111]

# dima = User(name=na, phone=ph)
# print(dima.name)
# print(dima.phone)
# print(dima.get_info())

# ###
# vika = Users(name="Vika", phone="111")
# print(vika.get_info())

# na = "Vika11111"
# ph = "23452"
# vika = Users(name=na, phone=ph)
# print(vika.get_info())
# print(vika.name)
# print(vika.phone)
# ###











################################
# from collections import UserDict


# class Field:#Батьківський клас
#     def __init__(self, name, phone):
#         self.nicname = name
#         self.phone = phone
    
#     def __str__(self):
#         return str(self.nicname)
    
# class Name(Field):
#     def __str__(self, name):
#         super().__init__(name)
#         return f"contact: {name}, phones: '; 'phone"

    # def __init__(self, name, phone) -> None:
        #     self.name = name
        #     self.phone = phone
            
        # def get_info(self):
        #     return f"'{self.name}': {self.phone}"
        
        

# class Phone(Field):
#     pass

# class Record:
#     def __init__(self, name):
#         self.name = Name(name)
#         self.phones = []
    
#     def __str__(self):
#         return f"contact: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# class AddressBook(UserDict):
# 		pass


# book = AddressBook()

# val = Name()  
# val = Field("Dima", 230498702)

# print(val)
# print(val.nicname)
# print(val.phone)


########### Завдання
# # Створення нової адресної книги
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
