a = int(input('введите a='))
b = int(input('введите b='))
c = int(input('введите c='))
if a < b + c and c < b + a and b < a + c:
    # print('треугольник существует')
    if a == b == c:
        print('треугольник равностороний')
    elif a == b or a == c or b == c:
        print('треугольник равнобедренный')
    elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2:
        print('треугольник прямоугольный')
    else:
        print('треугольник произвольный')
else:
    print('треугольник не существует')
