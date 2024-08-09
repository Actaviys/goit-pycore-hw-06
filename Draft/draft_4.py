from collections import UserDict


class AddressBook(UserDict): #Адресна книга
    
    def add_record(self, record): #Метод add_record, який додає запис до self.data.
        
        ##Так і не поняв як це працює 😐🤷‍♀️🙂##
        self.data[record.n] = record.phones # (##`1`)-Так приймається значення?
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




# class Field: #Базовий клас
#     def __init__(self, nam, pho=None):
#         self.nam = nam
#         self.pho = pho
#         self.res = {}
#         self.ph_ls_res.append(str(self.pho))
#         self.res[self.nam] = self.pho
        
        
#     def __str__(self):
#         return str(self.res)
        
        
        
        
# class Name(Field):
#     def __init__(self, names):
#         self.names = names
#         self.st_n = ""
#         self.st_n += self.names
#     def __str__(self):
#         return str(self.st_n)

# class Phone(Field):  
#     def __init__(self, phone=None):
#         self.phone = phone
#         self.pho = self.phone
    
#     def __str__(self):
#         return str(self.pho)


class Record:
    def __init__(self, n):
        self.n = n
        self.phones = []
        self.res = {}
        self.res[self.n] = self.phones
  
    
    def add_phone(self, ph=None): #Метод для додавання телефону
        self.ph = ph
        self.phones.append(self.ph)
        
        
    

    def __str__(self):
        return str(self.res)

    

        
book = AddressBook()#Створюю адресну книгу

sasha = Record("Sasha")
sasha.add_phone(3242343)
sasha.add_phone(55555555555555)


my_dict = {}
my_dict[sasha] = sasha # (##`1`)

print(f"\nRecord->{sasha}")#{sasha_phone}

book.add_record(sasha)

print(f"AddressBook-> {book}")
