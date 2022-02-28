a = int(input('введите a='))
b = int(input('введите b='))
c = 0
if b == 0 or a == 0 or a == b == 0:
    c = 0
    print(c)
elif b > 0 or a < 0 and b < 0:
    for i in range(b):
        c += a
    print(c)
elif b < 0:
    for i in range(a):
         c += b
print(c)
