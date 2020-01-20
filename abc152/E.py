# E - Flatten
# https://atcoder.jp/contests/abc152/tasks/abc152_e

import fractions 

N = int(input())
A = list(map(int, input().split()))
MODE = 10**9+7

def lcm(a, b):
    return a*b//fractions.gcd(a,b)

_lcm = 1
for a in A:
    _lcm = lcm(a, _lcm)

ret = 0
for a in A:
    ret += (_lcm // a)

print(ret%MODE)
