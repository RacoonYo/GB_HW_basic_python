class Car:
    speed = 60
    color = 'Grey'
    name = 'Swallow'
    is_police = False

    def go(self):
        return 'Car go'

    def stop(self):
        return 'Car stop'

    def turn(self, direction):
        return f'Car turned {direction}'

    def show_speed(self):
        return f'speed: {self.speed}'


class TownCar(Car):
    color = 'White'
    name = 'washtub'

    def __init__(self, speed):
        self.speed = speed

    def show_speed(self):
        if self.speed > 60:
            return f'over speed: {self.speed}'
        return f'speed: {self.speed}'


class SportCar(Car):
    color = 'White'
    name = 'flash'

    def __init__(self, speed):
        self.speed = speed


class WorkCar(Car):
    color = 'dirty'
    name = 'horse'

    def __init__(self, speed):
        self.speed = speed

    def show_speed(self):
        if self.speed > 40:
            return f'over speed: {self.speed}'
        return f'speed: {self.speed}'


class PoliceCar(Car):
    color = 'Blue'
    name = 'Ben'
    is_police = True

    def __init__(self, speed):
        self.speed = speed





