import sys
t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    S=str(num)
    GrtMul=0
    List=list()
    for i in range(len(S)):
        List.append(int(S[i]))
    for i in range(n-k+1):
        Mul=1
        for j in range (k):
            Mul*=List[i+j]
        if GrtMul<Mul:
            GrtMul=Mul
    print(GrtMul)
