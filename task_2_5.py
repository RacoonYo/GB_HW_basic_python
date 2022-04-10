source_list = [1.5, 25, 18.2, 33.5, 64, 23.18, 38.12, 25, 84.2, 36.4, 32, 15.03]
price_list = []

# part A
print('part A')
for price in source_list:
    kopecks = int(price % 1 * 100)
    price_list.append(f'{price // 1 : .0f} руб {str(kopecks).zfill(2)} коп')

print(', '.join(price_list), '\n')

# part B
print('part B')
print('ID до:', id(source_list))
source_list.sort()
print(source_list)
print('ID после:', id(source_list), '\n')

# part C
print('part C')
price_list_sort = sorted(source_list, reverse=True)
print(price_list_sort, '\n')

# part D
print('part D')
print(source_list[-5:])
