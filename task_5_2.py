n = int(input('введите число: '))
odd_to_15 = (num for num in range(1, n+1, 2))

print(list(odd_to_15))
