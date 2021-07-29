number = 5
a = 0
for el in range(number + 1):
    a = a + el
print(f'{a == number * (number + 1) / 2}')  # Вбиваем в принт уравнение и оно автоматически выдает булево значение
print(a)
