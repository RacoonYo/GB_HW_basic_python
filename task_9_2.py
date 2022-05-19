class Road:
    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    def mass_calc(self, depth):
        return self.__length * self.__width * depth/100 * 25


road_one = Road(5000, 20)
print(road_one.mass_calc(5))

road_on = Road(1000, 10)
print(road_on.mass_calc(2))

