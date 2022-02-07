a = int(input('введите a='))
b = int(input('введите b='))
c = int(input('введите c='))
d = b ** 2-4 * a * c
if d > 0:
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    print('x1=', x1)
    print('x2=', x2)
elif d == 0:
    x = -b / 2 / a
    print('x1=x2=', x)
else:
    print('действительных корней нет')

