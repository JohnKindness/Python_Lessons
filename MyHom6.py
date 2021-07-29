import random

number = random.randrange(0, 101)
i = 0

for el in range(10):
    answer_number = int(input('Введите число: '))
    i += 1
    if answer_number == number:
        print('Вы угадали!')
        break
    elif i == 10:
        print(f'Попытки закончились, верное число {number}')  # Делаем 2 проверки: 1) если совпал ответ, то конец цикла, если i = 10, то тоже конец, иначе игра продолжается и пишеться подсказка
    elif answer_number > number:
        print('Ваше число больше загаданного')
    elif answer_number < number:
        print('Ваше число меньше загаданного')
