# C - Next Prime
# https://atcoder.jp/contests/abc149/tasks/abc149_c

import math

MAX_X = 10**5 + 1000

# construct prime table, pb
pt = [True]*MAX_X
pt[0], pt[1] = False, False

for i in range(2, int(math.sqrt(MAX_X))+1):
    for j in range(2*i, MAX_X, i):
       pt[j] = False

# get primes
primes = [ idx for idx, num in enumerate(pt) if num == True]

X = int(input())

# find next prime
for prime in primes:
    if X <= prime:
        print prime
        break
