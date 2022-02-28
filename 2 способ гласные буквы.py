s = input('введите строку')
k = len(s)
c = 0
alpha = 'уаоэяиюёеы'
for i in range(k):
    if s[i] in alpha:
        c += 1
print(c)
