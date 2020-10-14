def isPalindrome(n):
    N=str(n)
    L=len(N)
    for i in range(L//2):
        if N[i]!=N[L-1-i]:
            return False
    return True
def Solution(n):
    for i in range(n-1,101100,-1):
        if isPalindrome(i):
            for j in range(101,1000):
                if i%j==0:
                    k=i//j
                    if (k%1000)==k:
                        return i
    return 0
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(Solution(n))
