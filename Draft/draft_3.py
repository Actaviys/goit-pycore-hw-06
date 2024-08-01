
from collections import UserDict
from collections.abc import Iterable
from typing import Any


class AddressBook(UserDict): #Адресна книга
    
    def add_record(self, value): #Метод add_record, який додає запис до self.data.
        self.value = value
        self.data.update(value)
    
    def find(self, fid): #Знаходить запис за ім'ям
        self.fid = fid
        for f in self.data:
            if f == fid:
                return self.data[fid]
                # return f"{f}: {self.data[fid]}"
        
    
    def delete(self, delt): #Видаляє запис за ім'ям.
        self.delt = delt
        self.data.pop(delt)
        return f"Delet: {delt}"




class Field: #Базовий клас
    def __init__(self, nam, pho=None):
        self.nam = nam
        self.pho = pho
        self.ph_ls_res = []
        self.res = {}
        self.ph_ls_res.append(str(self.pho))
        self.res[self.nam] = self.ph_ls_res
        # print(self.res)
        
        
    def __dir__(self) -> Iterable[str]:
        
        
        return dict(self.res)
        
        
    
        
        
        

        
book = AddressBook()#Створюю адресну книгу

dima = Field("Dima", 2343244)
print(dima)
# book.add_record(dima)


# dima_r = {"Dima": [9999]}
# book.add_record(dima_r) #№ 3 Записую по-> ключ:значення

# print(f"Field-> {dima}")
print(f"AddressBook-> {book}")










#########
# from collections import UserDict


# class AddressBook(UserDict): #Адресна книга
    
#     def add_record(self, value): #Метод add_record, який додає запис до self.data.
#         self.value = value
#         self.data.update(value)
    
#     def find(self, fid): #Знаходить запис за ім'ям
#         self.fid = fid
#         for f in self.data:
#             if f == fid:
#                 return f"{f}: {self.data[fid]}"
        
    
#     def delete(self, delt): #Видаляє запис за ім'ям.
#         self.delt = delt
#         self.data.pop(delt)
#         return f"Delet: {delt}"




# class Field: #Базовий клас
#     def __init__(self, nam, pho=None):
#         self.nam = nam
#         self.pho = pho
#         self.res = {}
#         self.res[nam] = pho

#     # def __str__(self):
#     #     return str(f"Field ->{self.res}")
    

# class Phone(Field):#Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
#     def __init__(self, phone):
#         super().__init__(phone)
#         self.phone = phone     
        
#     def __str__(self):
#         return str(self.phone)



# class Name(Field): #Для зберігання імені контакту
#     def __init__(self, name):
#         super().__init__(name)
#         self.name = name
        
    
#     def __str__(self):
#         return str(self.name)




# class Record:
#     def __init__(self, n):
#         self.n = Name(n)
#         self.ph = []
#         self.res = {}
    
#     def add_phone(self, p): #Метод для додавання телефону
#         self.p = Phone(p)
#         self.ph.append(str(self.p))
#         self.res[str(self.n)] = self.ph
#         return self.res
        
        
#     def remove_phone(self, remov): #Метод для видалення 
#         pass

#     def edit_phone(self, edit): #Метод для редагування
#         pass
        
#     def find_phone(self, find): #Пошуку об'єктів 'Phone'
#         pass
        
#     # def __str__(self):
#     #     return str(self.res)
        
        
#     # self.rlist = []
#     # self.rlist.append(name)
    
#     # def add_phone(self, phon):
#     #     self.phones.append(phon)
    
    
#     # def __str__(self):
#     #     r = f"{self.name}: {self.phones}"
#     #     self.res.update({self.name : self.phones})
#     #     return self.res
#     # # def __getstate__(self) -> object:
#     # #     return self.res
        
# book = AddressBook()#Створюю адресну книгу

# john_r = Record("Lyda") #"Lyda", 479274582
# john_r.add_phone(222222)
# john_r.add_phone(555555)
# print(john_r)

# # dima_r = {"Dima": [9999]}
# # book.add_record(dima_r) #№ 3 Записую по-> ключ:значення


# # lisa_r = {"lisa": [33333, 45444]}
# # book.add_record(lisa_r) #№ 3 Записую по-> ключ:значення

# # book.add_record(john_r)
# print(book)


# print("_________________________________________________________________________________")
# ###
# # Створення нової адресної книги
# book = AddressBook()#Створюю адресну книгу
# pho = [23423,1111111]
# nam = "Lisa"
# book.add_record(nam, pho) #№1 Записую по-> ключ:значення
# book.add_record("Lyda", 23423) #№2 Записую по-> ключ:значення
# lisa_r = {"lisa": 33333}
# book.add_record(lisa_r) #№ 3 Записую по-> ключ:значення
# print(f"AdresBook -> {book}")#Виводжу резльтат списку


# Створення запису для John
# john_r = Record("John")
# john_r.add_phone("1234567890")
# john_r.add_phone("5555555555")

# # # Додавання запису John до адресної книги
# book.add_record(john_r)
# print(f"Record -> {john_r}") 
# print(f"AdresBook -> {book}")#Виводжу резльтат списку



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



