a = int(input('введите трехзначное число a='))
b1 = a % 10
b2 = a // 10 % 10
b3 = a // 100
b = b1 + b2 + b3
print('сумма его цифр =', b)
