b=1000000000
c=1000000200
for a in range(b,c+1):
    k=0
    # for i in range(2,a//2+1):
    for i in range(2, int(a**0.5)+1):
        if a % i ==0:
            k+=1
            break
    if k==0:
        print(a, end=' ')
 