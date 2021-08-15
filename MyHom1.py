import collections

defdict = collections.defaultdict(list)
sum_factory = int(input('Введите количество предприятий: '))
avg = []
i = 0
for el in range(sum_factory):  # Тут мы пробегаемся столько раз, сколько предприятий задано
    some = []                  # , что бы собрать информацию про имя компаний и доходы
    name = input('Введите имя: ')
    for idx in range(4):
        profit = int(input(f'Введите сумму за {idx + 1} квартал: '))
        some.append(profit)
        i += profit  # Тут заносим весь профит всех пердприятий в переменнную
    avg.append(sum(some) / 4)  # В avg мы заносим поочередно среднее каждого предприятия
    defdict[name] = some

ex = list(defdict)
for item, sign in enumerate(avg):  # Сравниваем средние значения с общим средним значением
    if sign > i / (sum_factory * 4):
        print(f'В комании {ex[item]} прибыль выше среднего или равно среднему')
    elif sign <= i / (sum_factory * 4):
        print(f'В комании {ex[item]} прибыль ниже среднего')
