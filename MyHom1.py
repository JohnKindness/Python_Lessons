first_num = float(input('Введите 1 число: '))
second_num = float(input('Введите 2 число: '))
sign = input('Введите знак операции: ')

def some():
    first_num = float(input('Введите 1 число: '))
    second_num = float(input('Введите 2 число: '))
    sign = input('Введите знак операции: ')
    return first_num, second_num, sign

#Пишем цикл, который будет работать пока не сработает 'break'
while True:
    if sign == '+':
        print(f'{first_num + second_num}')
        first_num = float(input('Введите 1 число: '))
        second_num = float(input('Введите 2 число: '))
        sign = input('Введите знак операции: ')
    elif sign == '-':
        print(f'{first_num - second_num}')
        first_num = float(input('Введите 1 число: '))
        second_num = float(input('Введите 2 число: '))
        sign = input('Введите знак операции: ')
    elif sign == '*':
        print(f'{first_num * second_num}')
        first_num = float(input('Введите 1 число: '))
        second_num = float(input('Введите 2 число: '))
        sign = input('Введите знак операции: ')
    elif sign == '/': #Тут делаем еще одно отвлетвление if, чтобы не позволять делить на ноль
        if second_num != 0:
            print(f'{first_num / second_num}')
            first_num = float(input('Введите 1 число: '))
            second_num = float(input('Введите 2 число: '))
            sign = input('Введите знак операции: ')
        else:
            print('На ноль делить нельзя')
            second_num = float(input('Введите 2 число: '))
    elif sign == '0': #Тут как раз выходим из цикла когда знак равен 0
        break
    else:
        print('Не верное значение')
        sign = input('Введите знак операции: ')
