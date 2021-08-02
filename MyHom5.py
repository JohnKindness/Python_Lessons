numbers = [1, 3, 4, -1999, -100, 676, -4, 3]

for el in range(len(numbers)):  # Пробегаемся по массиву, как только найденный минимум найденный методом min() == эллементу массива, то пишем его и его индекс в массиве
    if min(numbers) == numbers[el]:
        min_place = el
        min_meaning = numbers[el]

print(min_place, min_meaning)
