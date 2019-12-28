# AtCoder abc148

## Tags:
###### tags: `atcoder`, `abc148`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - Round One](https://atcoder.jp/contests/abc148/tasks/abc148_a) | Python 2.7 | <span style="color:green">AC</span> |  77 bytes |  10 ms |  2568 KB |
| [Problem B - Strings with the Same Length](https://atcoder.jp/contests/abc148/tasks/abc148_b) | Python 2.7 | <span style="color:green">AC</span> |  140 bytes |  10 ms |  2568 KB |
| [Problem C - Snack](https://atcoder.jp/contests/abc148/tasks/abc148_c) | Python 2.7 | <span style="color:green">AC</span> |  225 bytes |  11 ms |  2568 KB |
| [Problem D - Brick Break](https://atcoder.jp/contests/abc148/tasks/abc148_d) | Python 2.7 | <span style="color:green"> AC </span> | 276 bytes | 130 ms | 20008 KB |
| [Problem E - Double Factorial](https://atcoder.jp/contests/abc148/tasks/abc148_d) | Python 2.7 | <span style="color:green"> AC </span> | 187 bytes | 10 ms | 2568 KB |
| [Problem F - Playing Tag on Tree](https://atcoder.jp/contests/abc148/tasks/abc148_d) | ? | ? | ? bytes | ? ms | ? KB |


## Solutions
### Problem A - Round One
```python
A = int(input())
B = int(input())

s = 1 + 2 + 3

print '{}'.format(s-A-B)
```

### Problem B - Strings with the Same Length
```python
N = int(input())
S, T = raw_input().split()

ret = ''

for n in range(N):
    ret += S[n]
    ret += T[n]

print '{}'.format(ret)
```

### Problem C - Snack
```python
def gcd(A, B):
    if B > A: 
        A, B = B, A

    if B == 0:
        return A
    else:
        return gcd(B, A%B)


A, B = map(int, raw_input().split())

gcdAB = gcd(A, B)

print '{}'.format(A*B/gcdAB)
```

### Problem D - Brick Break 
```python
N = int(input())
A = list()
 
A = [n for n in map(int, raw_input().split())]
    
cur = 1
cnt = 0
 
for a in A:
    if a == cur:
        cur += 1
    else:
        cnt += 1
 
if cnt == N and cur == 1:
    print '-1'
else:
    print '{}'.format(cnt)
```

### Problem E - Double Factorial
```python
N = int(input())

ret = 0

if N % 2 == 0:
    N //= 2
    while N > 0:
        N //= 5
        ret += N

print '{}'.format(ret)
```
