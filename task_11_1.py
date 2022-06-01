import re


class Number:
    def __init__(self, number: str):
        self.number = int(number)


class Date:
    def __init__(self, date: str):
        if re.fullmatch(r'(?:\d{2}-){2}\d{4}', date):
            self.date = date
        else:
            raise ValueError(f'date must be in the format dd-mm-yyyy')

    @classmethod
    def get_number(cls, date: str):
        if re.fullmatch(r'(?:\d{2}-){2}\d{4}', date):
            day, mouth, year = date.split('-')
            return [Number(day), Number(mouth), Number(year)]
        else:
            raise ValueError(f'date must be in the format dd-mm-yyyy')

    @staticmethod
    def check_valid(date: str):
        if re.fullmatch(r'(?:\d{2}-){2}\d{4}', date):
            day, mouth, year = date.split('-')
            day, mouth, year = int(day), int(mouth), int(year)
            if year > 0:
                if mouth in [1, 3, 5, 7, 8, 10, 12]:
                    return 0 < day < 32
                if mouth in [4, 5, 9, 11]:
                    return 0 < day < 31
                if mouth == 2:
                    return (0 < day < 28) or (day == 29 and year % 4 == 0)
            return False
        else:
            raise ValueError(f'date must be in the format dd-mm-yyyy')


print(Date.get_number('31-10-2022'))
print(Date.check_valid('31-11-2666'))
