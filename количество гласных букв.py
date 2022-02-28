s = input('введите строку')
k = len(s)
c = 0
for i in range(k):
    if s[i] == 'у' or s[i] == 'е' or s[i] == 'а' or s[i] == 'ю' or s[i] == 'э' or s[i] == 'я' or s[i] == 'и'\
            or s[i] == 'ы' or s[i] == 'о' or s[i] == 'ё':
        c += 1
print(c)
