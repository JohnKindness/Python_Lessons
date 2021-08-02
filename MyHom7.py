numbers = [2, 3, 65, -100, 1, 3, -1932]
mines_num = []

for num in range(2):  # Пробугаемся 2 раза по массиву, очищая и даобвляя минимальное значение
    mines_num.append(min(numbers))
    numbers.remove(min(numbers))

print(numbers)
print(mines_num)
