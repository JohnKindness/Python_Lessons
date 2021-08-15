class Translate:  # Создал класс в котором операторы сложения и умножения, так же метод
    def __init__(self, num='100'):  # который переводит числа в разные системы счисления
        self.num = num

    def __add__(self, other):
        return other + self.convert(self.num)

    def __mul__(self, other):
        return other * self.convert(self.num)

    def convert(self, n, to_base=10, from_base=16):
        D = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if isinstance(n, str):
            n = int(n, from_base)
        if n >= to_base:
            return self.convert(n // to_base, to_base) + D[n % to_base]
        else:
            return D[n]


first_num = Translate('A2')
second_num = Translate('C4F')
third_num = Translate()
fourth_num = Translate()
first_num = first_num.convert('A2', to_base=10, from_base=16)
second_num = second_num.convert('C4F', to_base=10, from_base=16)
sum = int(first_num) + int(second_num)
multiplication = int(first_num) * int(second_num)
third_num = third_num.convert(sum, to_base=16, from_base=10)
fourth_num = fourth_num.convert(multiplication, to_base=16, from_base=10)
print(third_num)
print(fourth_num)
# Вызываем метод из класса для перевода чисел в другие системы и совершаем сложение и уменожение
