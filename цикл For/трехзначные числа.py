k = 0
k2 = 0
k5 = 0
k6 = 0
for i in range(100, 999 + 1):
    print(i, end=' ')
    k += 1  # k = k + 1 k++
    if i % 2 == 0:
        k2 += 1
    if i % 5 == 0:
        k5 += 1
    if i % 3 == 0 and i % 2 == 0:
        k6 += 1

print()  # как будто нажали кнопку ввода - для перехода на новую строчку
print('Количество трёхзначных чисел равно', k)
print('Количество трёхзначных четных чисел равно', k2)
print('Количество трёхзначных кратных 5', k5)
print('Количество трёхзначных кратных 2 и 3', k6)
