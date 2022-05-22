from abc import ABC, abstractmethod


class Clothes(ABC):
    consumption_all_fabric = 0

    @abstractmethod
    def get_fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Clothes.consumption_all_fabric += self.get_fabric_consumption

    @property
    def get_fabric_consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, height):
        self.height = height
        Clothes.consumption_all_fabric += self.get_fabric_consumption

    @property
    def get_fabric_consumption(self):
        return self.height * 2 + 0.3


one_clothes = Suit(10)
two_clothes = Coat(5)

print(one_clothes.get_fabric_consumption)
print(two_clothes.get_fabric_consumption)

print(Clothes.consumption_all_fabric)  # the total amount of fabric spent on all pieces of clothing
