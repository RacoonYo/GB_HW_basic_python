'''
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на
русский язык. Например:
#>>> num_translate("one")
"один"
#>>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить
информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или
снаружи.
'''


def num_translate(number: str):
    translate_book = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                      'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десят'}

    return translate_book.get(number)


if __name__ == "__main__":
    print(num_translate('one'))
    print(num_translate('six'))
    print(num_translate('zsix'))
    print(num_translate('Six'))
    print(num_translate('Zsix'))
    

