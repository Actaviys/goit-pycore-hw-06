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



###############################
# from collections import UserDict

# class AddressBook(UserDict): #Адресна книга
#     pass

# class Field:#Батьківський клас
#     def __init__(self, value):
#         self.nicname = value
#         self.value = value
    
#     def __str__(self):
#         return str(self.value)
    
# class Name(Field):
#     pass

# class Phone(Field):
#     pass

# class Record:
#     def __str__(self):
#         return f"'name': ''"
    
# val = Field("fe.er \nqw")
 
# book = AddressBook()#Створюю адресну книгу

# print(val.value)