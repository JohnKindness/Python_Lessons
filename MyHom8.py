year = int(input('Введите год: '))

if year % 100 != 0 and year % 4 == 0:
    print('Это вискосный год')
else:
    print('Год не вискосный')
