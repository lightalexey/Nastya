a = int(input('введите a='))
k = 0
for i in range(1, a + 1):
    if a % i == 0:
        print(i, end=' ')
        k += 1
print()
print('количество делителей', k)
