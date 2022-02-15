a = int(input('введите a='))
s = 0
for i in range(1, a):
    if a % i == 0:
        s += i
if s == a:
    print('число является совершенным')
else:
    print('число не является совершенным')

