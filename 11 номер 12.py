s = '1' + '9' * 99
while '19' in s or '299' in s or '399' in s:
    if '19' in s:
        s = s.replace('19', '2', 1)
    if '299' in s:
        s = s.replace('299', '3', 1)
    if '399' in s:
        s = s.replace('399', '1', 1)
print(s)
