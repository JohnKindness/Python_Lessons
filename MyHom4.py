numbers = [2, 7, 7, 7, 7, 1, 100, 100, 1]
repeat = []

for el in numbers:  # Пробегаемся по массиву и заносим количество повторов каждой цифр в массиве, игнорируя повторы
    num = numbers.count(el)
    repeat.append(num)
for idx in range(len(repeat)):  # При первой же встрече max числа ищем по индексу в numbers и выводим
    if max(repeat) == repeat[idx]:
        some = numbers[idx]

print(some)
