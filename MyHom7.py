a = float(input('Введите длину первой стороны: '))
b = float(input('Введите длину второй стороны: '))
c = float(input('Введите длину третьей стороны: '))

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Треугольник с данными сторонами может существовать!')
            if a == b and a != c:
                print('Треугольник равнобедренный')
            elif a == b and a == c:
                print('Треугольник равносторонний')
            else:
                print('треугольник разносторонний')
else:
    print('Треугольник с данными сторонами не может существовать')
