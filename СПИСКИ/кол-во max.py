from random import randrange

a = []
print('исходный список')
n = 15
for i in range(n):
    number = randrange(50) - 15
    a.append(number)
    print(a[i], end=' ')
print()
max = a[0]
k = 0
for i in range(n):
    if a[i] > max:
        a[i] = max
k += 1
print(k)
