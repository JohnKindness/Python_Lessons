import math
first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')

place1 = ord(first_letter) - 96
place2 = ord(second_letter) - 96
long = math.fabs(place1 - place2)
print(f'Место буквы "{first_letter}" это {place1}, место буквы "{second_letter}" это {place2}')
print(f'Количество букв между введенными буквами {int(long - 1)}')
