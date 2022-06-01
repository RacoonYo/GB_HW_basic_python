import re
from classes import Printer, Scanner, Copier, Warehouse



warehouse_dict = {}
printers_dict = {}
scanners_dict = {}
copiers_dict = {}



def is_number(txt: str):
    try:
        float(txt)
        return True
    except ValueError:
        return False


def create_new_warehouse():
    while True:
        name = input('Please, enter name warehouse: ')
        if warehouse_dict.get(name):
            print("this name already exists, enter a unique name")
            continue
        else:
            break

    location = input(f'Please, enter where is location {name}: ')

    while True:
        size = input('Please, enter size your warehouse: ')
        if not is_number(size):
            print("size is number!!!")
            continue
        else:
            break

    warehouse_dict[name] = Warehouse(location, size)
    return name


if __name__ == '__main__':
    print('creating new warehouse')
    name = create_new_warehouse()
    while True:
        command = input('enter "1" if you want to add the printer to the warehouse\n'
                        'enter "2" if you want to add the scaner to the warehouse\n'
                        'enter "3" if you want to add the copier to the warehouse\n'
                        'enter "M" if you want to look what put to the warehouse\n'
                        'enter "Q" if you want to exit\n')

        if command.strip() == '1':
            model = input('please, enter printer model: ')
            while True:
                dimension = input('please, enter dimension in format WWW*HHH*LLL: ')
                if
            warehouse_dict[name].add_to_warehouse()


