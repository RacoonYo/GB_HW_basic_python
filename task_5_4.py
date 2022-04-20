src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 155]


def more_rear_compr(input_list: list):
    result = [input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1]]
    return result


def more_rear_gen(input_list: list):
    result = (input_list[i] for i in range(1, len(input_list)) if input_list[i] > input_list[i - 1])
    yield result


if __name__ == '__main__':
    print(more_rear_compr(src))

    print(list(*more_rear_gen(src)))
