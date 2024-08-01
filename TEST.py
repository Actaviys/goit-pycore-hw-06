

class Human:
    name = ''

    def voice(self):
        print(f"Hello! My name is {self.name}")


class Developer(Human):
    field_description = "My Programming language"
    language = ""

    def make_some_code(self):
        return f"{self.field_description} is {self.value}"


class PythonDeveloper(Developer):
    value = "Python"
    


class JSDeveloper(Developer):
    value = "JavaScript"


p_dev = PythonDeveloper()
p_dev.name = 'Bob'
p_dev.voice()  # Hello! My name is Bob
print(p_dev.make_some_code())  # My Programming language is Python
print(p_dev.value)

js_dev = JSDeveloper()
js_dev.make_some_code()  # My Programming language is JavaScript
print(js_dev.value)



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