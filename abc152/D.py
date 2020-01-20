# D - Handstand 2
# https://atcoder.jp/contests/abc152/tasks/abc152_d

import numpy as np

N = int(input())
tb = np.zeros((10, 10), dtype=int)

for n in range(1, N+1):
    n = str(n)
    lhs, rhs = int(n[0]), int(n[-1])
    tb[lhs][rhs] += 1

ret = 0
for lhs in range(1, 10):
    for rhs in range(1, 10):
       ret += tb[lhs][rhs] * tb[rhs][lhs]

print(ret) 

