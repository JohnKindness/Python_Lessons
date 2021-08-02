numbers = [8, 2, 15, 6, 4, 2, 7, 10]
places = []

for el in range(len(numbers)):  # Пробегаемся по длине массива и усли четное, то добавляем индекс в массив place
    if numbers[el] % 2 == 0:
        places.append(el)
print(places)
