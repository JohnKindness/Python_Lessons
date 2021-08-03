import cProfile
n = int(input('Введите число: '))
m = int(input('Введите число: '))

# Решето Эратосфена
def first():
    a = []
    for i in range(n + 1):
        a.append(i)

    a[1] = 0

    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    print(a)

# Альтернативный способ
def second():
    some = []
    num = []
    for idx in range(n + 1):
        some.append(idx)

    some = some[2:]

    for el in some:
        i = 0
        for item in range(2, m + 1):
            if el % item == 0:
                i += 1
                if i > 1:
                    num.append(el)
                    break
    numbers = set(some) - set(num)
    print(numbers)


cProfile.run('first()')
cProfile.run('second()')
# Примерно решение проблемы через Решето Эратосфена быстрее в 12 раз. При введении числа 1000 видна это инофрмация.
# Во втором алгоритме цикл в цикле, что очень нагружает процессор.
