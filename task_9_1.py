import time


class TrafficLight:
    __color = 'RED'

    def running(self, color=__color, counter=-1):  # можно задавать начальный цвет и количество изменений
        while counter:                            # цвета до конца работы. По умолчанию бесконечная работа.
            print('color', color.upper())
            if color.upper() == 'RED':
                time.sleep(7)
                color = 'YELLOW'
            elif color.upper() == 'YELLOW':
                time.sleep(2)
                color = 'GREEN'
            elif color.upper() == 'GREEN':
                time.sleep(5)
                color = 'RED'
            counter -= 1
        return print('Traffic light is stopped')


my_tr_light = TrafficLight()
my_tr_light.running(color="Green")


