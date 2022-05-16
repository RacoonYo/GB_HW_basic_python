from functools import wraps


def type_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = ''
        for arg in args:
            result += f'{func.__name__}({arg}: {type(arg)}), '
        return result[:-2]

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


if __name__=='__main__':
    a = calc_cube(5, 7, 9, 'a')
    print(a)