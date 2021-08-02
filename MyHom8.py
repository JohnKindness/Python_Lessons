number = input('Введите 16 чисел через пробел: ')  # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
second_list = []
first_list = []
new_number = number.split()
i = 0
for el in new_number:  # Пробегаемся по данным введенным пользователем и  заносим их в массив
    if i < 3:
        first_list.append(el)
        i += 1
    else:
        first_list.append(el)
        second_list.append(first_list)
        first_list = []
        i = 0
a = 0
for el in second_list:  # Тут добавляем пятый эллемент в подмассив, который является суммой всей строки
    for idx in el:
        a += int(idx)
    el.append(str(a))
    a = 0

print(f'{" ".join(second_list[0])}\n{" ".join(second_list[1])}\n{" ".join(second_list[2])}\n{" ".join(second_list[3])}')
