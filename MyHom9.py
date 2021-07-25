first_num = float(input('Введите 1 число: '))
second_num = float(input('Введите 2 число: '))
third_num = float(input('Введите 3 число: '))

if third_num >= first_num >= second_num or second_num >= first_num >= third_num:
    print(f'Среднее: {first_num}')
elif first_num >= second_num >= third_num or third_num >= second_num >= first_num:
    print(f'Среднее: {second_num}')
elif second_num >= third_num >= first_num or first_num >= third_num >= second_num:
    print(f'Среднее: {third_num}')
