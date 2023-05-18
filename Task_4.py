# Реализуйте класс Truck (грузовик). Грузовик может перевозить посылки - Box из предыдущего задания
# •	Импортиуйте модуль task_3_box из предыдущего задания.
# •	Создайте несколько экземпляров класса Box.
# •	Проверьте работу методов класса Box
# •	Создайте класс Truck (грузовик), который будет иметь несколько атрибутов, присущих грузовику.
# •	Реализуйте атрибут capacity (емкость), в котором будет реализовано хранилище посылок (Box): [box1, box2 ...]
# •	Переопределите методы __str__, __add__, __sub__ для реализации отображения грузовика,
# загрузки и выгрузки посылок.
# •	Продемонстрируйте работу класса Truck.


from Task_3_box import Box

class Truck:
    def __init__(self, capacity):
        self.__capacity = capacity

    def __str__(self):
        return f'Емкость грузовика: {len(self.__capacity)} посылок'

    def add(self, box):
        self.__capacity.append(box)

    def sub(self, box):
        self.__capacity.remove(box)

truck = Truck([])
a = Box('a', 'Нижнекамск', 'Москва')
b = Box('b', 'Москва', 'Нижнекамск')
truck.add(b_1)
truck.add(b_2)
print(truck)
print("_________________________________________")
truck.sub(b_1)
print(truck)

