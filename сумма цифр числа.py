a = int(input('введите a='))
s = k = 0
b = a % 10
while a > 0:
    s1 = a % 10
    s += s1
    a //= 10
    k += 1
print(s, k)
print(b)
