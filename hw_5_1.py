
# 5.1. Создайте любой класс с произвольным количеством подклассов,
# экземпляров, атрибутов и методов- как минимум один атрибут должен
# быть с уровнем доступа private. Соответственно, для получания
# значений этого атрибута нужно использовать методы get и set

#создаем класс Person
class Person ():
    #создаем первый метод
    def __init__(self, name, age, occupation, sex):
        #создаем атрибуты
        self.name = name
        self.age = age
        self.occupation = occupation
        self.sex = sex
    #создаем второй метод
    def pastime(self, hobby):
        return f'{self.name} plays {hobby}'
    #создаем третий метод с уровнем доступа private
    def __marriage(self, wife):
        return f'{self.name} is married to {wife}'
    #создаем четвертый метод
    def marriage_to(self,wife):
        self.wife = wife
        return self.__marriage(self.wife)
    #создаем подкласс Сolleague класса Person
class Сolleague(Person):
    #создаем атрибут подкласса Сolleague с уровнем доступа private
    __job_position = "Developer"
    def job(self, company):
        self.company = company
        return f'I work with {self.name} in {self.company}'
    #создаем метод get
    def get_job_position(self):
        return self.__job_position
    #создаем метод set
    def set_job_position(self, new_position):
        self.__job_position = new_position
#создаем экземпляр класса Person
Man = Person ('Andrey', 23, 'QA', 'male')
#создаем второй экземпляр класса Person
Woman = Person ('Alla', 35, 'back-end', 'female')
#создаем экземпляр подкласса Сolleague
Officemate = Сolleague('Diana', 29, 'Designer', 'female')

print(Man.name)
print(Man.age)
print(Man.occupation)
print(Man.sex)
print(Man.pastime('tennis'))
print(Man.marriage_to('Christina'))
print(Woman.name)
print(Woman.age)
print(Woman.occupation)
print(Woman.sex)
print(Officemate.job('Google'))
print(Officemate.pastime('Football'))
print(Officemate.get_job_position())
print(Officemate.set_job_position('QA'))
print(Officemate.get_job_position())
