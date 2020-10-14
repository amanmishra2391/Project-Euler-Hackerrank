from bisect import bisect
from math import sqrt
LIMIT = 2500000
sieve = [True] * LIMIT
primes = []
for number in range(2, int(sqrt(LIMIT))):
    if sieve[number]:
        primes.append(number)
        for multiple in range(number * number, LIMIT, number):
            sieve[multiple] = False
for number in range(int(sqrt(LIMIT)), LIMIT):
    if sieve[number]:
        primes.append(number)
T = int(input())
for _ in range(T):
    N = int(input())
    index = bisect(primes, N)
    print(sum(primes[:index]))
