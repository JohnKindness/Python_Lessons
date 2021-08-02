import random
num_1 = 5
num_2 = 5
matrix_1 = []
min_mean = []
for el in range(num_1):  # Составляем с помощью метода random рандомную таблицу 5 на 5
    matrix_2 = []
    for num in range(num_2):
        number = f'{random.random() * 100:.0f}'
        matrix_2.append(number)
    matrix_1.append(matrix_2)

for idx in matrix_1:  # Затем отбираем минимальные значения из подмассивов и выносим в отдельный массив
    min_mean.append(min(idx))

print(min_mean)
print(max(min_mean))  # Выводим значение максимального эллемента из минимальных
print(matrix_1)
