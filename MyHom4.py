import random
first_num = float(input('Введите первое число: '))
second_num = float(input('Введите второе число: '))
symbol1 = input('Введите первый символ символ: ')
symbol2 = input('Введите второй символ символ: ')

x = random.randrange(int(first_num), int(second_num))
y = random.uniform(first_num, second_num)
z = random.randrange(ord(symbol1), ord(symbol2))

print(f'Случайное целое число: {x}')
print(f'Случайное вещественное {y:.3f}')
print(f'Случайный символ {chr(z)}')
