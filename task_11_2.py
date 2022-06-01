class DivZeroError(Exception):
    def __str__(self):
        return "Can't divide by zero"


def division():
    while True:
        print('************\nFor exit enter V')
        number_one = input('Enter number: ')
        if number_one == 'V':
            exit(2)

        number_two = input('Enter number: ')
        if not int(number_two):
            try:
                raise DivZeroError
            except DivZeroError as e:
                print(e)
                continue
        print(f'Result: {int(number_one) / int(number_two)}')


division()




