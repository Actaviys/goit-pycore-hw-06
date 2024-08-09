"""
# Клас AddressBook:
# Реалізовано метод add_record, який додає запис до self.data.
# Реалізовано метод find, який знаходить запис за ім'ям.
# Реалізовано метод delete, який видаляє запис за ім'ям.


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
        self.data[record] = record #Записую в self.data
        
    
    def find(self, fid): #Знаходить запис за ім'ям
        self.fid = fid #
        for f in self.data: #Пробігаюсь циклом
            if f == fid: #Перевіряю на співпадіння
                return self.data[fid] #
                # return f"{f}: {self.data[fid]}"
        
    
    def delete(self, delt): #Видаляє запис за ім'ям.
        self.delt = delt
        self.data.pop(delt)
        return f"Delet: {delt}"

    # def __str__(self) -> str:
    #     return str(self.data)




class Field: #Базовий клас
    def __init__(self, names, phones=None):
        self.names = names
        self.phones = phones
            
            
class Name(Field):
    pull_n = " "
    def __init__(self, names):
        self.names = names
        self.pull_n = self.names
        
    def __str__(self):
        return str(self.pull_n)
      
     
class Phone(Field): #Перевірка на пра
    pull_p = " "
    def __init__(self, phone):
        self.phone = phone
        self.pull_p = self.phone

    def __str__(self) -> str:
        return str(self.phone)
        


class Record:
    result = {}
    
    def __init__(self, nam):
        self.nam = Name(nam)
        self.phon_list = []
        self.result[str(self.nam)] = self.phon_list
        # self.res = Field.result
        
    def add_phone(self, phon=None): #Метод для додавання телефону
        self.phon = Phone(phon)
        self.phon_list.append(str(self.phon))      
        
    def __str__(self) -> str:
        return str(self.result)


        
book = AddressBook()#Створюю адресну книгу

dima = Record("Dima")
# lisa = Record("Lisa")
dima.add_phone(233444322)
dima.add_phone(111111111)

# my_dict = {}
# my_dict[dima] = dima
# print(my_dict)

# book.add_record(dima)
# book.add_record(lisa)

print(f"Record-> {dima}")
# print(f"Record-> {lisa}")

book.add_record(dima)
print(f"AddressBook-> {book}")
