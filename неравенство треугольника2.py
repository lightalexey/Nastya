a = int(input('введите a='))
b = int(input('введите b='))
c = int(input('введите c='))
if a < b + c:
    if c < b + a:
        if  b < a + c:
         print('треугольник существует')
        else:
            print('треугольник не существует')
    else:
        print('треугольник не существует')
else:
    print('треугольник не существует')