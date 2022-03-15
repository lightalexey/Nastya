s = '8' * 1000
while '888' in s or '999' in s:
    if '888' in s:
        s = s.replace('888', '9', 1)
    elif '999' in s:
        s = s.replace('999', '8', 1)
print(s)
