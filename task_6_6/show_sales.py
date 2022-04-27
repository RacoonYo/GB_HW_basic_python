import sys


def show_sales(start=None, end=None):
    with open('bakery.csv', 'r', encoding='UTF-8') as f:
        show = f.read().split('\n')
        show.pop()
        return show[start: end]


if __name__ == '__main__':
    start = end = None
    if len(sys.argv) > 1:
        start = int(sys.argv[1]) - 1

    if len(sys.argv) > 2:
        end = int(sys.argv[2])

    print(*show_sales(start, end), sep='\n')
