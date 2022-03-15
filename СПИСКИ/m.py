from random import randrange
a = []
print('Исходный список:')
n = 10
for i in range(n):
    number = randrange(101) - 50 # [-50;50]
    a.append(number)
    print(a[i], end=' ')
print()
maximum=a[0]
imax=0
minimum=a[0]
for i in range(n):
    if a[i]>maximum:
        maximum=a[i]
        imax=i
    if a[i]<minimum:
        minimum=a[i]
print(maximum,imax)
print(minimum)
print(max(a))