numbers = [3, 4, 200, 199, 23, 1]

for el in range(len(numbers)):  # Пробегаемся по массиву и ищем max и min значения, запоминая их
    if numbers[el] == max(numbers):
        max_index = el
    elif numbers[el] == min(numbers):
        min_index = el
        min_meaning = numbers[el]

numbers[min_index] = numbers[max_index]  # Меняем местами значение
numbers[max_index] = min_meaning
print(numbers)
