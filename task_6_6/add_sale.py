import sys

sales_for_day = sys.argv[1]

with open('bakery.csv', 'a', encoding='UTF-8') as f:
    f.write(f'{sales_for_day}\n')
