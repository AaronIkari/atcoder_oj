# AtCoder abc118

## Tags:
###### tags: `atcoder`, `abc118`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - White Cells](https://atcoder.jp/contests/abc118/tasks/abc118_a) | Python 2.7 | <span style="color:green">AC</span> |  128 bytes |  10 ms |  2568 KB |
| [Problem B - Can you solve this?](https://atcoder.jp/contests/abc118/tasks/abc118_b) | Python 2.7 | <span style="color:green">AC</span> |  458 bytes |  275 ms |  19564 KB |
| [Problem C - Energy Drink Collector](https://atcoder.jp/contests/abc121/tasks/abc121_c) | Python 2.7 | <span style="color:green">AC</span> |  328 bytes |  90 ms |  12624 KB |
| [Problem D - Match Matching](https://atcoder.jp/contests/abc118/tasks/abc118_d) | ? | ? |  ? bytes |  ? ms |  ? KB |


## Solutions
### Problem A - B +/- A
```python
A, B = map(int, raw_input().split())

if B%A == 0:
    print '{}'.format(A+B)
else: # B%A != 0
    print '{}'.format(B-A)
```

### Problem B - Foods Loved by Everyone 

```python
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
```

### Problem C - Monsters Battle Royale
```
N = int(input())
A = set(map(int, raw_input().split()))

while len(A) != 1:

    # minimum number of A
    minA = min(A)

    # next round A
    nA = set()
    nA.add(minA)

    for Ai in A:
        if Ai == minA: continue
        if Ai % minA != 0:
            nA.add(Ai%minA)

    # update for next round
    A = nA

print '{}'.format( list(A)[-1])
```
