a = int(input('введите a='))
for i in range(100, 999 + 1):
    b1 = i % 10
    b2 = i // 10 % 10
    b3 = i // 100
    b = b1 + b2 + b3
    if a == b:
        print(i, end=' ')
