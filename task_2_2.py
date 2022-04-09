source_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

marker = 0  # отслеживает был ли элемент цифрой
i = 0

for element in source_list:
    if element.lstrip('+-').isdigit():
        if 0 < int(element) < 10:
            if element[0] == '+' or element[0] == '-':
                source_list[i] = f'{element[0]}0{element[1]}'
            else:
                source_list[i] = f'0{element}'
        source_list.insert(i + 1, '"')
        marker = 1
        i += 1

        continue

    if marker == 1:
        source_list.insert(i - 1, '"')
        marker = 0

    i += 1

new_string = ' '.join(source_list)
print(new_string)


