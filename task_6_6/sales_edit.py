from sys import argv


with open('bakery.csv', 'r+', encoding='UTF-8') as f:
    f.readline()
    len_line = f.tell()
    f.seek((int(argv[1]) - 1) * 6, 0)
    print(f.tell())
    if f.readline():
        f.seek((int(argv[1]) - 1) * 6, 0)
        f.write(argv[2])
    else:
        print('not found index')