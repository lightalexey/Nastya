k = 0
k2 = 0
for i in range(10, 99 + 1):
    print(i, end=' ')
    k += 1  # k = k + 1 k++
    if i % 2 == 0:
        k2 += 1

print() # как будто нажали кнопку ввода - для перехода на новую строчку
print('Количество двухзначных чисел равно', k)
print('Количество двухзначных четных чисел равно', k2)
