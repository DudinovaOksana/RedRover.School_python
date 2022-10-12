# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов
# и выводит их построчно в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def biuld_profile_user(**kwargs):
    data = {}
    for key, value in kwargs.items():
        data[key] = value
    return data
user_profile = biuld_profile_user(name = "John", last_name = "Smith", age = "35", position = "web developer")
print(user_profile)