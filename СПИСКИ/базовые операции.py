from random import randrange
a = []
print('Исходный список:')
n = 10
for i in range(n):
    number = randrange(11) - 5 # [-5;5]
    a.append(number)
    print(a[i], end=' ')
print()
# код начинается отсюда...
p = 1
summa = 0
sp = 0
k = 0
for i in range(n):
    if a[i]>0:
        sp +=a[i]
        k +=1
    summa += a[i]
    if a[i]!=0:
        p *= a[i]

print('Сумма всех элементов списка равна', summa)
print('Произведение всех  не нулевых элементов списка равна', p)
print('Сумма положительных элементов списка равна', sp)
print('среднее арифметическое', summa/n)
print('положительных элементов', k)