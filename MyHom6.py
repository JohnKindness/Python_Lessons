numbers = [1, -999, 2, 300, 4, -10, -100, 600, 100, 3]

for el in range(len(numbers)):  # Пробегаемся и ищем место в массиве максимального и минимального значения
    if min(numbers) == numbers[el]:
        min_mean = el
    elif max(numbers) == numbers[el]:
        max_mean = el

if min_mean < max_mean:  # Делаем проверку если вначале будет большее или меньшее число.
    answer = sum(numbers[min_mean + 1:max_mean])
else:
    answer = sum(numbers[max_mean + 1:min_mean])
print(answer)
