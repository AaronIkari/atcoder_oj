# AtCoder abc149

## Tags:
###### tags: `atcoder`, `abc149`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - String](https://atcoder.jp/contests/abc149/tasks/abc149_a) | Python 2.7 | <span style="color:green">AC</span> |  43 bytes |  10 ms |  2568 KB |
| [Problem B - Greedy Takahashi](https://atcoder.jp/contests/abc149/tasks/abc149_b) | Python 2.7 | <span style="color:green">AC</span> |  203 bytes |  10 ms |  2696 KB |
| [Problem C - Next Prime](https://atcoder.jp/contests/abc149/tasks/abc149_c) | Python 2.7 | <span style="color:green">AC</span> | 356  bytes |  68 ms |  4996 KB |
| [Problem D - Prediction and Restriction](https://atcoder.jp/contests/abc149/tasks/abc149_d) | Python 3.4.3 | <span style="color:orange"> AC </span> | 814 bytes | 201 ms | 22604 KB |
| [Problem E - Handshake](https://atcoder.jp/contests/abc149/tasks/abc149_e) | Python 2.7 | <span style="color:orange"> WA </span> | 543 bytes | 2130 ms | 799600 KB |
| [Problem F - Playing Tag on Tree](https://atcoder.jp/contests/abc149/tasks/abc149_f) | ? | ? | ? bytes | ? ms | ? KB |


## Solutions
### Problem A - String
```python
S, T = raw_input().split()

print '{}'.format(T+S)
```

### Problem B - Greedy Takahashi
```python
A, B, K = map(int, raw_input().split())

if K >= A+B:
    print '0 0'
elif K >= A:
    K -= A
    print '0 {}'.format(B-K)
else:
    print '{} {}'.format(A-K, B)
```

### Problem C - Next Prime
```python
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
```

### Problem D - Prediction and Restriction 
```python
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

def opt(seg):
    # dp[STEP][R/P/S]
    dp = [ [-1, -1, -1] for _ in range(len(seg))]

    dp[0][0] = (R if seg[0] == 's' else 0)
    dp[0][1] = (P if seg[0] == 'r' else 0)
    dp[0][2] = (S if seg[0] == 'p' else 0)

    for i in range(1, len(seg)):
        dp[i][0] = (R if seg[i] == 's' else 0) + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = (P if seg[i] == 'r' else 0) + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = (S if seg[i] == 'p' else 0) + max(dp[i-1][0], dp[i-1][1])

    return max(dp[-1])

segs = list()

for K_idx in range(K):
    segs.append( T[K_idx::K] )

print('{}'.format(sum(map(opt, segs))))
```


