# AtCoder abc125

## Tags:
###### tags: `atcoder`, `abc125`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [A - Biscuit Generator](https://atcoder.jp/contests/abc125/tasks/abc125_a) | Python 2.7 | <span style="color:green">AC</span> |  83 bytes |  10 ms |  2568 KB |
| [B - 	Resale](https://atcoder.jp/contests/abc125/tasks/abc125_b) | Python 2.7 | <span style="color:green">AC</span> |  206 bytes |  10 ms |  2568 KB |
| [C - GCD on Blackboard](https://atcoder.jp/contests/abc125/tasks/abc125_c) | Python 2.7 | <span style="color:green">AC</span> |  605 bytes |  204 ms |  13700 KB |
| [D - Flipping Signs](https://atcoder.jp/contests/abc125/tasks/abc125_d) | Python 2.7 | <span style="color:green">AC</span> |  339/871 bytes |  76/454 ms |  11320/114244 KB |

## Solutions
### Problem A - Biscuit Generator
```python
A, B, T = map(int, raw_input().split())
print '{}'.format( int((T+0.5)/A) * B)
```

### Problem B - Resale

```python
N = int(raw_input())

V = map(int, raw_input().split())
C = map(int, raw_input().split())

X_Y = 0

for i in range(N):
    if V[i] - C[i] > 0:
        X_Y += V[i] - C[i]

print '{}'.format(X_Y)
```

### Problem C - GCD on Blackboard
```python
N = int(input())
A = list(map(int, raw_input().split()))

def gcd(m,n):
    return m if n == 0 else gcd(n, m%n)

L = [0] * (N+1)
R = [0] * (N+1)

# L: list
# boundary: L[0] = 0, L[N-1] = 0
# L[i]: previous (i-1)-th gcd value, i = [0, ..., N-2]
for i in range(N-1):
    L[i+1] = gcd(L[i], A[i])

# R: list
# boundary: R[0] = 0, R[N-1] = 0
# R[i]: last (N-i)-th gcd value, i = [N-1, ..., 1]
for i in range(N-1, 0, -1):
    R[i] = gcd(R[i+1], A[i])

max_gcd = 0
for i in range(N):
    if gcd(L[i], R[i+1]) > max_gcd:
        max_gcd = gcd(L[i], R[i+1])

print '{}'.format(max_gcd)
```


### Problem D - Flipping Signs
```python
N = int(input())
A = list(map(int, raw_input().split()))

ng_cnt = 0

for i in range(N):
    if A[i] < 0:
        ng_cnt += 1
        A[i] = -A[i]

if ng_cnt % 2 == 0:
    print '{}'.format( sum(A) )
else:
    print '{}'.format( sum(A) - min(A)*2)
```

### Problem D - Flipping Signs | DP method
```python
import sys
sys.setrecursionlimit(1000000)

N = int(input())
A = list( map(int, raw_input().split()) )

rcd = dict()

# dynamic programming, dp(current_position, (i-1)-th_sign)
def dp(pos, sign):

    # boundary condition
    if pos == N-1:
        if sign == 0:
            return A[pos]
        else:
            return -A[pos]

    # if visit (pos, sign) state before
    if (pos, sign) in rcd:
        return rcd[(pos, sign)]

    elif sign == 0:
        # memorize
        rcd[(pos, sign)] = max( dp(pos+1, 0) + A[pos], dp(pos+1, 1) - A[pos])
        return rcd[(pos, sign)]

    else: # st == 1
        # memorize
        rcd[(pos, sign)] = max( dp(pos+1, 0) -  A[pos], dp(pos + 1, 1) + A[pos])
        return rcd[(pos, sign)]

print '{}'.format( dp(0,0) )
```
