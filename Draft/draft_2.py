


from collections import UserDict
from collections.abc import Iterable


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
        self.res[nam] = pho
        
        
    # def __str__(self) -> str:
    #     print(str(self.ph_ls_res))
    #     return str(self.res)
    

class Phone(Field):#Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    def __init__(self, phone):
        super().__init__(phone)
        self.phone = phone      
        self.ph_ls_res.append(str(self.pho))  
        
    # def __str__(self):
    #     return str(self.phone)



class Name(Field): #Для зберігання імені контакту
    def __init__(self, name):
        self.name = name
        self.nam = self.name
    
    def __str__(self):
        return str(self.name)




class Record:
    def __init__(self, n):
        self.n = Name(n)
        
        
    
    def add_phone(self, p): #Метод для додавання телефону
        self.p = Phone(p)
        return list(self.p.ph_ls_res)
        
        # return f"Add phone: {self.ph_ls_res}"
        
    # def remove_phone(self, remov): #Метод для видалення 
    #     self.remov = remov
    #     ier = 0
    #     for r in self.ph_ls_res: 
    #         ier += 1
    #         if ier == int(remov):
    #             self.ph_ls_res.remove(r)       
    #     return self.ph_ls_res

    # def edit_phone(self, old, new): #Метод для редагування
    #     self.old = old
    #     self.new = new
    #     # self.nam_lis = 
    #     for e in self.old:
    #         print(e, "+++")
            
        
        
        
    def find_phone(self, find): #Пошуку об'єктів 'Phone'
        pass
        
        
    # def __str__(self):
    #     return self.p.ph_ls_res
        
        
        
    # self.rlist = []
    # self.rlist.append(name)
    
    # def add_phone(self, phon):
    #     self.phones.append(phon)
    
    
    # def __str__(self):
    #     r = f"{self.name}: {self.phones}"
    #     self.res.update({self.name : self.phones})
    #     return self.res
    # # def __getstate__(self) -> object:
    # #     return self.res
        
book = AddressBook()#Створюю адресну книгу

# john_r = Record("Lyda") #"Lyda", 479274582
# john_r.add_phone(222222)
# john_r.add_phone(555555)
# print(john_r)
# print()
# print(john_r.remove_phone(2))


# dima_r = {"Dima": [9999]}
# book.add_record(dima_r) #№ 3 Записую по-> ключ:значення

# dima_r = {"Lisa": [6345, 345435]}
# book.add_record(dima_r) #№ 3 Записую по-> ключ:значення

# book.add_record(john_r)
# print(book,"\n")

# dima = book.find("Lyda")

# print(dima)
# dima.edit_phone("1234567890", "1112223333")
print("\n",book)

print("_________________________________________________________________________________")
###






# from collections import UserDict
# from collections.abc import Iterable


# class AddressBook(UserDict):
        
#     def add_record(self, value):
#         self.data = value
    
       
    
#     def __str__(self):
#         return str(self.data)




# class Field:
#     def __init__(self, nam, pho=None):
#         self.nam = nam
#         self.pho = pho
#         self.res = {}
#         self.res[nam] = pho

#     # def __str__(self):
#     #     return str(f"Field ->{self.res}")
    

# class Phone(Field):
#     def __init__(self, phone):
#         super().__init__(phone)
#         self.phone = phone     
        
#     def __str__(self):
#         return str(self.phone)



# class Name(Field):
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
    
#     def add_phone(self, p):
#         self.p = Phone(p)
#         self.ph.append(str(self.p))
        

#     def __str__(self):
#         self.res[str(self.n)] = self.ph
#         return str(self.res)
        
        
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
# # print(john_r)

# lisa_r = {"lisa": [33333, 45444]}
# book.add_record(lisa_r) #№ 3 Записую по-> ключ:значення

# book.add_record(john_r)
# print(book.data)
# print(book.data)
# # print(book)
        
    

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
