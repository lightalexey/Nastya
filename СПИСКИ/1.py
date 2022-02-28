# a1 a2 a3 ...
a = []
print('Исходный список:')
print(a)
n = int(input('Введи количество элементов:'))
for i in range(n):
    number = int(input('Введи элемент:'))
    a.append(number)
print('Исходный список:')
for i in range(n):
    print(a[i], end=' ')
print()
print('2 способ. Исходный список:')
print(a)