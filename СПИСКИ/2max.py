from random import randrange
a = []
print('исходный список:')
n = 15
for i in range(n):
        number = randrange(100)-38
        a.append(number)
        print(a[i], end=' ')
print()
imax = 0
max=a[0]
tmax=0
k=0
for i in range(n):
    if a[i]>max:
        max=a[i]
        imax=i
print(max)
for i in range(n):
    if imax!=i and a[i]>tmax:
        tmax=a[i]
k+=1
print(tmax)
print(k)
