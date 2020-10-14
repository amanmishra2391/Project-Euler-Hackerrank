def LCM(x,y):
    c=1
    a=2
    while (x!=1 or y!=1):
        if x%a==0 or y%a==0:
            c=c*a
            if x%a==0:
                x=x//a
            if y%a==0:
                y=y//a
        else:
            a+=1
    return c

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    L=1
    for i in range(2,n+1):
        L=LCM(L,i)
    print(L)
