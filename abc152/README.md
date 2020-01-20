# AtCoder abc152

## Tags:
###### tags: `atcoder`, `abc152`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - AC or WA](https://atcoder.jp/contests/abc152/tasks/abc152_a) | Python 3.4.3 | <span style="color:green">AC</span> |   82 bytes |  17 ms | 2940  KB |
| [Problem B - Comparing Strings](https://atcoder.jp/contests/abc152/tasks/abc152_b) | Python 3.4.3 | <span style="color:green">AC</span> |   131 bytes |  17  ms | 2940 KB |
| [Problem C - Low Elements](https://atcoder.jp/contests/abc152/tasks/abc152_c) | Python 3.4.3 | <span style="color:green">AC</span> |   175 bytes |   109 ms | 24744  KB |
| [Problem D - Handstand 2](https://atcoder.jp/contests/abc152/tasks/abc152_d) | Python 3.4.3 | <span style="color:green">AC</span> |  400 bytes | 309 ms |  21368 KB |
| [Problem E - Flatten](https://atcoder.jp/contests/abc152/tasks/abc152_e) | ? | <span style="color:green"> AC </span> | 263 bytes | 1891 ms | 6112 KB |
| [Problem F - Tree and Constraints](https://atcoder.jp/contests/abc152/tasks/abc152_f) | ? | ? | ? bytes | ? ms | ? KB |


## Solutions
### Problem A - AC or WA 
```python
N, M = map(int, input().split())
if N == M:
  print('Yes')
else:
  print('No')
```

### Problem B - Comparing Strings 
```python
a, b = map(int, input().split())

ret = [str(a)*b, str(b)*a]
ret.sort()

print(ret[0])
```

### Problem C - Low Elements 
```python
N = int(input())
P = list(map(int, input().split()))
 
cur_min = P[0]
ret = 1
for i in range(1, N):
  if P[i] < cur_min:
    cur_min = P[i]
    ret += 1
 
print(ret)
```

### Problem D - Handstand 2 
```python
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
```

### Problem E - Flatten
```python
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
```

---

```python
# (Correct answer, but TLE) 
from math import *
from collections import defaultdict

MAX_Ai = 10**6
MAX_PRIME = ceil(sqrt(MAX_Ai))
MODE = 10**9+7

N = int(input())
A = map(int, input().split())


def get_prime():
    # prime table
    ptb = [True] * MAX_PRIME
    ptb[0] = ptb[1] = False

    for i in range(2, ceil(sqrt(MAX_PRIME)) + 1):
        for j in range(i*2, MAX_PRIME, i):
            ptb[j] = False

    P = [ i for i, v in enumerate(ptb) if v == True]

    return P

def prime_factorization(n, P):
    factor = defaultdict(int)
    for p in P:
        while n % p == 0:
            factor[p] += 1
            n //= p

    if n != 1:
        factor[n] += 1

    return factor

def main():
    P = get_prime()    

    A_fact = list()
    lcm = defaultdict()
    for a in A:
        a_fact = prime_factorization(a, P)
        A_fact.append(a_fact)
        for prime, power in a_fact.items():
            if prime not in lcm:
                lcm[prime] = power
            else:
                if lcm[prime] < power:
                    lcm[prime] = power

    ret = 0
    for a_fact in A_fact:
        b_fact = {key: lcm[key] - a_fact.get(key, 0) for key in lcm.keys()}
        tmp = 1
        for prime, power in b_fact.items():
            tmp *= prime**power
            tmp %= MODE
        ret += tmp
        ret %= MODE

    print(ret)


if __name__ == "__main__":
    main()
```
