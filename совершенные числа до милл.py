for a in range(6,10**9+1):
    s = 0
    for i in range(1, a):
        if a % i == 0:
            s += i
    if s == a:
        print(a)


