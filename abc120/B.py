# B - K-th Common Divisor
# https://atcoder.jp/contests/abc120/tasks/abc120_b
# 1WA
import math

MAX = 100

def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

A, B, K = map(int, raw_input().split())
gcdAB = gcd(A, B)

cnt = 0
for n in range(gcdAB, 0, -1):
    if gcdAB % n == 0:
        cnt += 1
        if cnt == K:
            print '{}'.format(n)
            break
