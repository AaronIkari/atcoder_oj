# B - Foods Loved by Everyone
# https://atcoder.jp/contests/abc118/tasks/abc118_b

import numpy as np

N, M = map(int, raw_input().split())

rcd = [[False for c in range(M+1)] for r in range(N)]

for i in range(N):
    KA = list(map(int, raw_input().split()))
    K = KA[0]
    for j in range(1, K+1):
        rcd[i][ KA[j] ] = True

rcd = np.array(rcd)

cnt = 0
for c in range( len(rcd[0]) ):
    if sum(rcd[:,c]) == N:
        cnt += 1

print '{}'.format(cnt)
