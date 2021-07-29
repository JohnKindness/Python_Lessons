numbers = [1, 24, 35, 23, 87, 97, 100001, 999]

sum_numbers = []
for el in numbers:
    b = 0
    a = list(str(el))  # Берем число и заносим его в массив по отдельным числам
    for long in range(len(a)):
        b += int(a[long])
    sum_numbers.append(b)  # Затем раздробив число на цыфры складываем их и заносим в общий массив, где хранятся суммы чисел
print(max(sum_numbers))  # Просто достаем из массива большее число
