number_one = float(input('Введите 1 число: '))
number_two = float(input('Введите 2 число: '))
change = input('Укажите "+" если хотите сложить числа или укажите "*" если хотите умножить числа ')

if len(str(f'{number_one:.0f}')) == 3 and len(str(f'{number_two:.0f}')) == 3:
    if change == '+':
        print(number_one + number_two)
    if change == '*':
        print(number_one * number_two)
else:
    print('Не верный формат числа')
