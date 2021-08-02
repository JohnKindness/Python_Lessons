numbers = [2, 3, 4, 5, 6, 7, 8, 9]
some = []

for el in range(2, 100):  # Пробегаемся по чисалам с 2-99, а затем 8 раз поробегаемся и проверяем деление без остатка
    for num in range(8):
        if el % numbers[num] == 0:
            some.append(numbers[num])

for el in numbers:
    print(f'{el} - {some.count(el)}')  # Выводим знаечение каждого из элеметнов, пробегаясь по массиву some
