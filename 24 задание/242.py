f=open('24_demo.txt')
s= f.read()
r=1
t=1
for i in range(len(s)-1):
    if s[i]==s[i+1]=='X':
        t+=1
    else:
        if t>r:
            r=t
        t=1
print(max(r,t))