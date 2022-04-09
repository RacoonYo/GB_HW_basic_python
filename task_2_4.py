source_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
               'директор аэлита']

for element in source_list:
    print(f'Привет, {element.split()[-1].capitalize()}!')
