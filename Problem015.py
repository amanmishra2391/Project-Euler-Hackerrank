from math import factorial as fact
for _ in range(int(input())):
    n,m=list(map(int,input().split(" ")))
    print((fact(n+m)//(fact(n) * fact(m))) % 1000000007)
