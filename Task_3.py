# Создайте класс Box (посылка), у которого будет приватные атрибуты:
# •	postcode (номер отправления),
# •	name (имя отправителя),
# •	from_city (город отправителя),
# •	target_city (город назначения).
# •	Реализуйте методы, которые будут давать возможность доступа к приватным атрибутам.
# •	Реализуйте метод, который будет давать возможность менять город назанчения
# •	Назовите модуль task_3_box и сохраните его

import random

class Box:

    def __init__(self, name, from_city, target_city):
        self.__postcode = random.randint(1000000, 9999999)
        self.__name = name
        self.__from_city = from_city
        self.__target_city = target_city

    def postcode(self):
        return self.__postcode

    def name(self):
        return self.__name

    def from_city(self):
        return self.__from_city

    @property
    def target_city(self):
        return self.__target_city

    @target_city.setter
    def target_city(self, new_target_city):
        self.__target_city = new_target_city
        return self.__target_city


b = Box('Егор', 'Нижнекамск', 'Москва')
print(f"Номер отправления: {b.postcode()}")
print("_________________________")
print(f"Имя отправителя: {b.name()}")
print("_________________________")
print(f"Город отправителя: {b.from_city()}")
print("_________________________")
print(f"Город назначения: {b.target_city}")
print("_________________________")

b.target_city = 'Рим'
print(f"Город назначения изменен: {b.target_city}")
