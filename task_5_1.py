def odd_nums(num: int):
    for result in range(1, num, 2):
        yield result


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))

print('################\n')

odd_to_15 = odd_nums(15)
for i in odd_to_15:
    print(i)