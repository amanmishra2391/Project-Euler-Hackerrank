t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    S=0
    d = (n-1) // 3
    S+= 3 * (d * (d+1)) // 2
    d = (n-1) // 5
    S+= 5 * (d * (d+1)) // 2
    d = (n-1) // 15
    S-= 15 * (d * (d+1)) // 2
    print(S)
