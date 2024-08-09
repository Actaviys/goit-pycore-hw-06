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
        # self.ph_ls_res.append(str(self.pho))
        self.res[self.nam] = self.pho
        # print(self.res)
        
        
    def __str__(self):
        return str(self.res)
        
        
class Name(Field):
    def __init__(self, names):
        self.names = names
        
    def __str__(self):
        return str(self.names)


class Phone(Field):  
    def __init__(self, phone):
        self.phone = phone
    
    def __str__(self):
        return str(self.phone)
        
    


class Record:
    def __init__(self, n):
        self.name = Name(n)
        self.phones = []
        
        
    
    def add_phone(self, ph): #Метод для додавання телефону
        self.ph = Phone(ph)
        self.phones.append(self.ph)
        
        

    # def __str__(self):
    #     return str(self.phones)
    # def __str__(self):
    #     return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

        
book = AddressBook()#Створюю адресну книгу

dima = Field("Dima", 2343244)
lisa = Field("Lisa", [333333333, 22222222])

sasha = Record("Sasha")
# sasha.add_phone(777777)
# sasha.add_phone(88888)
# # sasha.a



##
my_dict = {}
my_dict[dima] = dima # (##`1`)
# my_dict[dima.nam] = dima.pho # (##`2`)
##

# sasha.
print(f"Record-> {sasha}")
# book.add_record(dima)
# book.add_record(lisa)

# print(f"Field-> {dima}^^|^^{lisa}^^|^^{sasha}")

# print(f"AddressBook-> {book}")





################################
# class Human:
#     name = ''

#     def voice(self):
#         print(f"Hello! My name is {self.name}")


# class Developer(Human):
#     field_description = "My Programming language"
#     language = ""

#     def make_some_code(self):
#         return f"{self.field_description} is {self.value}"


# class PythonDeveloper(Developer):
#     value = "Python"
    


# class JSDeveloper(Developer):
#     value = "JavaScript"


# p_dev = PythonDeveloper()
# p_dev.name = 'Bob'
# p_dev.voice()  # Hello! My name is Bob
# print(p_dev.make_some_code())  # My Programming language is Python
# print(p_dev.value)

# js_dev = JSDeveloper()
# js_dev.make_some_code()  # My Programming language is JavaScript
# print(js_dev.value)



################################################
# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
        
        

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight

#     def change_color(self, color_in):
#         self.color_in = color_in
#         Animal.color = color_in

# irst_animal = Animal("Nick", 2)
# irst_animal.change_color("red")
# print(irst_animal.color)


#####################
# class Animal:
    
#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#         self.color = "white"
        
        

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight
        
#     def change_color(self, color_in):
#         self.color_in = color_in
#         self.color = self.color_in
        

# first_animal = Animal("Nick", 2)
# first_animal.change_color("red")
# second_animal = Animal("Archy", 12)
# second_animal.change_color("red")
# print(first_animal.color)
# print(second_animal.color)

# ########################################################################
# class Animal:
#     color = "white"

#     def __init__(self, nickname, weight):
#         self.nickname = nickname
#         self.weight = weight
#         self.color = "white"
        

#     def say(self):
#         pass

#     def change_weight(self, weight):
#         self.weight = weight
        
#     def change_color(self, color_in):
#         self.color_in = color_in
#         self.color = self.color_in
#         # return str(self.color)
        
        
# first_animal = Animal("Nick", 2)
# first_animal.change_color("red")
# second_animal = Animal("Archy", 12)
# # print(first_animal.change_color("red"))
# print(first_animal.color)
# ############################################################################
# res = {"Katya": 23423}

# name = "Dima"
# phone = 234234324


# res[name] = phone

# res ["Lyda"] = 2149832479823

# print(res)