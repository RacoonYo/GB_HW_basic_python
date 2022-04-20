from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б'
]

# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]

def gen_tut_klass(tutors: list, klasses: list):  # реализация логики самостоятельно
    if len(tutors) > len(klasses):
        while len(tutors) != len(klasses):
            klasses.append(None)

    for i in range(0, len(tutors)):
        yield tutors[i], klasses[i]


# реализация в одну строку
oneline_impl = zip_longest(tutors, klasses)


if __name__ == '__main__':
    for i in gen_tut_klass(tutors, klasses):
        print(i)

    print('\n######################\n')

    gen_klass = gen_tut_klass(tutors, klasses)
    print(next(gen_klass))
    print(next(gen_klass))
    print(next(gen_klass))
    print(next(gen_klass))


    print('\none line implementation')
    print(next(oneline_impl))
    print(next(oneline_impl))
    print(next(oneline_impl))
    print(next(oneline_impl))
    print(next(oneline_impl))
    print(next(oneline_impl))
    print(next(oneline_impl))

