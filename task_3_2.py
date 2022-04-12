'''
 *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать
корректную работу с числительными, начинающимися с заглавной буквы — результат тоже
должен быть с заглавной. Например:
#>>> num_translate_adv("One")
"Один"
#>>> num_translate_adv("two")
"два"
'''


def num_translate_adv(number: str):
    translate_book = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десят'}

    if number[0].isupper():
        return str(translate_book.get(number.lower())).capitalize()

    return translate_book.get(number)


if __name__ == "__main__":
    print(num_translate_adv('One'))
    print(num_translate_adv('six'))
    print(num_translate_adv('sidx'))
    print(num_translate_adv('Dsix'))
    print(num_translate_adv('Seven'))