
b=100
c=200
for a in range(b,c+1):
    k=0
    for i in range(2,a//2+1):
        if a % i ==0:
            k+=1
            break
    if k==0:
        print(a, end=' ')
 