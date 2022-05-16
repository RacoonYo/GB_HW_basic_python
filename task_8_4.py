from functools import wraps


def val_checker(val_func=True):

    def _val_checker(func):

        @wraps(func)
        def wrapper(arg):
            if val_func(arg):
                return func(arg)

            else:
                raise ValueError(f'wrong value {arg}')

        return wrapper

    return _val_checker


@val_checker(val_func=lambda x: x > 4)
def calc_cube(x):
    return x ** 3


if __name__ == '__main__':
    a = calc_cube(5)
    print(a)
    print(calc_cube.__name__)

    a = calc_cube(3)
    print(a)
    print(calc_cube.__name__)

