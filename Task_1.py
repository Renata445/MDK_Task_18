# Создайте класс Person с приватными атрибутами name, age, surname.
# Реализуйте методы name, age, surname, которые будут давать доступ к аналогичным приватным атрибутам.
# Создайте сеттер, который будет давать возможность поменять атрибут age.

class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def name(self):
        return self.__name

    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age
        return self.__age


p = Person('Shrek', 'Linkol', 59)
print(p.name())
print(p.surname())
print(p.age)
print("______________________________________")
p.age = 60
print(p.age)
