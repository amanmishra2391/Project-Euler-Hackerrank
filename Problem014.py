import math
Lengths ={0:0,1:0,2:1,4:2}
Largest_Number = [0,1]
def Collatz (N):
    if N in Lengths.keys():
        return Lengths[N]
    if N%2 == 0:
        a = math.log(N,2)
        if a.is_integer():
            Lengths[N] = a
        else:
            Lengths[N] = 1+Collatz(N//2)
    else :
        Lengths[N] = 1+Collatz(3*N + 1)
    return Lengths[N]
for i in range(int(input())):
    N = int(input())
    for j in range(len(Largest_Number), N + 1):
        Collatz(j)
        if Lengths[j] >= Lengths[Largest_Number[j-1]]:
            Largest_Number.insert(j, j)
        else:
            Largest_Number.insert(j, Largest_Number[j - 1])
    print (Largest_Number[N])
