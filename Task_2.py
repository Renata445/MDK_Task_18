# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта - одежда (Cloth), которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто Coat) и рост (для костюма Suit). Это могут быть обычные числа V и H соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# •	для пальто V/6.5+0.5
# •	для костюма 2H+0.3 Проверить работу этих методов на реальных данных.
# Выполнить общий подсчет расхода ткани, который пойдет на пошив всех костюмов и всех пальто соответственно.
# Реализовать абстрактыне классы для основных классов проекта и проверить работу декоратора @property.
# Подсказка:
# •	Воспользуйтесь абстрактным классом при создании класса Cloth
# •	Определите абстрактные методы подсчета количества ткани
# •	Количество ткани reserved сделайте атрибутом класса ( определяется вне конструктора)

from abc import ABC, abstractmethod


class Cloth(ABC):
    reserved = 0

    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    def total_fabric_consumption(self):
        return self.fabric_consumption() + self.reserved


class Coat(Cloth):
    def fabric_consumption(self):
        return self.size / 6,5 + 0,5


class Suit(Cloth):
    def fabric_consumption(self):
        return 2 * self.size + 0,3


coat1 = Coat('Пальто', 250)
suit1 = Suit('Костюм', 324)
print(coat1.name, coat1.size, coat1.total_fabric_consumption)
print("______________________________________________________________")
print(suit1.name, suit1.size, suit1.total_fabric_consumption)
print("______________________________________________________________")
total_fabric_consumption = coat1.total_fabric_consumption + suit1.total_fabric_consumption
print('Общий расход тканей: ', total_fabric_consumption)

