class ValidData(Exception):
    def __str__(self):
        return 'you can enter only numbers'


result_list = []

while True:
    print('**************\nFor exit enter "stop"')
    number = input('Enter number: ')
    if number.lower().strip() == 'stop':
        print(result_list)
        exit()
    elif number.isdecimal():
        result_list.append(number)
    else:
        try:
            raise ValidData
        except ValidData as e:
            print(e)
