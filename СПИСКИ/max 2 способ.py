from random import randrange
a = []
print('Исходный список:')
n = 10
for i in range(n):
    number = randrange(101) - 50 # [-50;50]
    a.append(number)
    print(a[i], end=' ')
print()
imax=0
for i in range(n):
    if a[i]>a[imax]:
        imax=i
print(imax,a[imax])
