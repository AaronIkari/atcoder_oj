# B - K-th Common Divisor
# https://atcoder.jp/contests/abc120/tasks/abc120_b
# 1WA
import math

MAX = 100

def gcd(A, B):
    if B > A:
        A, B = A, B

    if B == 0:
        return A

    return gcd(B, A-(A/B)*B)

prime_table = [True]*MAX
prime_table[0] = prime_table[1] = False
for i in range(2, int(math.sqrt(MAX)) + 1):
    for j in range(i*2, MAX, i):
        prime_table[j] = False
primes = [i_idx for i_idx in range(len(prime_table)) if prime_table[i_idx] == True]

A, B, K = map(int, raw_input().split())
gcdAB = gcd(A, B)

factors = set()
factors.add(gcdAB)
factors.add(1)

for prime in primes:
    if prime > gcdAB:
        break
    if gcdAB % prime == 0:
        factors.add(prime)
        factors.add(gcdAB/prime)

factors = list(factors)
factors.sort(reverse=True)

print '{}'.format(factors[K - 1])
