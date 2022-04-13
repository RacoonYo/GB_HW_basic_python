'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный",
"мягкий"]
Например:
#>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
'''

from random import choice, randint

# ВАРИАНТ РЕШЕНИЯ №1
def get_jokes(amount: int):
    jokes_dict = {'nouns': ["автомобиль", "лес", "огонь", "город", "дом"],
                  'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
                  'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]}
    jokes_list = []
    len_nouns = len(jokes_dict['nouns'])
    len_adverbs = len(jokes_dict['adverbs'])
    len_adjectives = len(jokes_dict['adjectives'])

    while amount > 0:
        jokes_list.append(f"{jokes_dict['nouns'][randint(0, len_nouns - 1)]} "
                          f"{jokes_dict['adverbs'][randint(0, len_adverbs - 1)]} "
                          f"{jokes_dict['adjectives'][randint(0, len_adjectives - 1)]}")
        amount -= 1

    return jokes_list


# ВАРИАНТ РЕШЕНИЯ №2
def get_jokes_1(amount: int):
    jokes_dict = {'nouns': ["автомобиль", "лес", "огонь", "город", "дом"],
                  'adverbs': ["сегодня", "вчера", "завтра", "позавчера", "ночью"],
                  'adjectives': ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]}
    jokes_list = []
    interim_list = []

    while amount > 0:
        for key in jokes_dict.keys():
            interim_list.append(f"{choice(jokes_dict[key])}")

        jokes_list.append(' '.join(interim_list))
        interim_list.clear()
        amount -= 1

    return jokes_list



if __name__ == "__main__":
    print(get_jokes(2))
    print(get_jokes_1(3))
