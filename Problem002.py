import sys
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a=1
    b=2
    S=2
    while 1:
        b+=a
        a=b-a
        if b>n:
            break
        elif b%2==0:
            S+=b
    print(S)
