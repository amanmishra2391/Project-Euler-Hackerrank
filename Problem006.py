t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    Sum=(((n-1)*n*(n+1)*((3*n)+2))//12)
    print(abs(Sum))
