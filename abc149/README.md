# AtCoder abc149

## Tags:
###### tags: `atcoder`, `abc149`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - String](https://atcoder.jp/contests/abc149/tasks/abc149_a) | Python 2.7 | <span style="color:green">AC</span> |  43 bytes |  10 ms |  2568 KB |
| [Problem B - Greedy Takahashi](https://atcoder.jp/contests/abc149/tasks/abc149_b) | Python 2.7 | <span style="color:green">AC</span> |  203 bytes |  10 ms |  2696 KB |
| [Problem C - Next Prime](https://atcoder.jp/contests/abc149/tasks/abc149_c) | Python 2.7 | <span style="color:green">AC</span> | 356  bytes |  68 ms |  4996 KB |
| [Problem D - Prediction and Restriction](https://atcoder.jp/contests/abc149/tasks/abc149_d) | Python 2.7 | <span style="color:orange"> WA </span> | 715 bytes | 52 ms | 7648 KB |
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
