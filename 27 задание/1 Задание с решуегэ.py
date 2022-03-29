f = open('27-A_demo.txt')
n = int(f.readline())
summa = 0
delta = 10 ** 6
for i in range(n):
    s = f.readline()
    s1, s2 = s.split()
    s1, s2 = int(s1), int(s2)
    summa += max(s1, s2)
    if abs(s1 - s2) < delta and abs(s1 - s2) % 3 != 0:
        delta = abs(s1 - s2)
# print(summa, summa % 3)
print(summa - delta)