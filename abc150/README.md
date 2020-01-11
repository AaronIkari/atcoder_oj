# AtCoder abc150

## Tags:
###### tags: `atcoder`, `abc150`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - 500 Yen Coins](https://atcoder.jp/contests/abc150/tasks/abc150_a) | Python 3.4.3 | <span style="color:green">AC</span> |  380 bytes |  58 ms |  11300 KB |
| [Problem B - Count ABC](https://atcoder.jp/contests/abc150/tasks/abc150_b) | Python 3.4.3 | <span style="color:green">AC</span> |  158 bytes |  17 ms |  2940 KB |
| [Problem C - Count Order](https://atcoder.jp/contests/abc150/tasks/abc150_c) | Python 3.4.3 | <span style="color:green">AC</span> | 232  bytes |  27 ms |  8052 KB |
| [Problem D - Semi Common Multiple](https://atcoder.jp/contests/abc150/tasks/abc150_d) | Python 3.4.3.3 | <span style="color:orange"> AC </span> | 814 bytes | 201 ms | 22604 KB |
| [Problem E - Change a Little Bit](https://atcoder.jp/contests/abc150/tasks/abc150_e) | Python 3.4.3 | <span style="color:orange"> ? </span> | ? bytes | ? ms | ? KB |
| [Problem F - Xor Shift](https://atcoder.jp/contests/abc150/tasks/abc150_f) | ? | ? | ? bytes | ? ms | ? KB |


## Solutions
### Problem A - 500 Yen Coins
```python
K, X = map(int, input().split())

if 500 * K >= X:
    print('Yes')
else:
    print('No')
```

### Problem B - Count ABC 
```python
N = int(input())
S = input()

ret = 0

for i in range(0, N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        ret += 1

print(ret)
```

### Problem C - Count Order 
```python
# C - Count Order
# https://atcoder.jp/contests/abc150/tasks/abc150_c

from itertools import permutations 

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

perm = list(permutations([i+1 for i in range(N)]))

print(abs(perm.index(P) - perm.index(Q)))
```

### Problem D - Semi Common Multiple 
```python
N, M = map(int, input().split())
A = list(set(map(lambda x : int(x)//2, input().split())))

def _gcd(a, b):
    return a if b == 0 else _gcd(b, a%b)

def _lcm(a,b):
    return (a*b) // _gcd(a,b)

lcm = A[0] 
for ai in A[1:]:
    lcm = _lcm(lcm, ai)

ret = (M//lcm + 1)//2

for ai in A[1:]:
    if (lcm // ai) % 2 == 0:
        ret = 0
        break 

print(ret)
```


