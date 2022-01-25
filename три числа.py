a = int(input('Введи а='))
b = int(input('Введи b='))
c = int(input('Введи а='))
if c < a > b:
    print(a)
if a < b and b > c:
    print(b)
if a < c and b < c:
    print(c)
print(max(a,b,c))

