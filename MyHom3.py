x1 = float(input('Введите "x1" первой точки: '))
y1 = float(input('Введите "y1" первой точки: '))
x2 = float(input('Введите "x2" первой точки: '))
y2 = float(input('Введите "y2" первой точки: '))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f'Уравнение прямой: y = {k:.2f}*x + {b:.2f}')
