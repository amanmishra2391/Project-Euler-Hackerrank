def isPrime(N):
    a=2
    k=N//2
    while k>=a:
        if N%a==0:
            return False
        a+=1
        k=N//a
    return True
t = int(input().strip())
List=[2,3,5,7,11,13,17,19]
for a0 in range(t):
    n = int(input().strip())
    if n<=len(List):
        print(List[n-1])
    else:
        i=len(List)
        k=List[i-1]
        while i<n:
            k+=1
            if isPrime(k):
                i+=1
                List.append(k)
        print(k)
