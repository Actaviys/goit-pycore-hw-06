"""
Клас AddressBook:
Реалізовано метод add_record, який додає запис до self.data.
Реалізовано метод find, який знаходить запис за ім'ям.
Реалізовано метод delete, який видаляє запис за ім'ям.


Клас Record:
Реалізовано зберігання об'єкта Name в окремому атрибуті.
Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - edit_phone/пошуку об'єктів Phone - find_phone.


Клас Phone:
Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
"""

from collections import UserDict


class AddressBook(UserDict): #Адресна книга
    
    def add_record(self, record): #Метод add_record, який додає запис до self.data.
        
        ##Так і не поняв як це працює 😐🤷‍♀️🙂##
        self.data[record.nam] = record.pho # (##`1`)-Так приймається значення?
        # self.data[record] = record # (##`2`)-А так приймається об'єкт?
        #Чи навпаки 🤔🤔#
    
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
        
        
    def __str__(self):
        return str(self.res)
        
         

        
book = AddressBook()#Створюю адресну книгу

dima = Field("Dima")
lisa = Field("Lisa", [333333333, 22222222])
my_dict = {}
#####\/#####
my_dict[dima] = dima # (##`1`)
# my_dict[dima.nam] = dima.pho # (##`2`)
print(my_dict)
#####/\#####
book.add_record(dima)
book.add_record(lisa)

print(f"Field-> {dima}")

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