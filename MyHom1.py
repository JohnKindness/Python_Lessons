import random
chose = int(input('Введите число, повтор которого Вам интересен: '))
numbers = []
for idx in range(10):
    numbers.append(random.randrange(1, 10))


def first():  # Первая реализация
    i = 0
    for el in numbers:
        if el == chose:  # Обычная проверка на совпадение при пробегании по ряду чисел
            i += 1
    return i


def second():  # Вторая реализация (заведома нелогичнее)
    some = []
    for item in numbers:
        some.append(numbers.count(item))
    if numbers.count(chose) != 0:
        return f'{some[numbers.index(chose)]}'
    else:
        return '0'


print(numbers)


if __name__ == '__main__':
    import timeit
    print(first())
    print(second())
    print(f'Скорость первой реализации {timeit.timeit("first()", setup="from __main__ import first")}')
    print(f'Скорость второй реализации {timeit.timeit("second()", setup="from __main__ import second")}')
# В итоге получаеться, что второй алгоритм работает примерно в 5 раз медленее, что является критической ошибкой
