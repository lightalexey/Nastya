from random import randrange
a = []
print('Исходный список:')
n = 10
for i in range(n):
    number = randrange(101) - 50 # [-50;50]
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
summa = 0
for i in range(n):
    summa += a[i]

print('Сумма всех элементов списка равна', summa)