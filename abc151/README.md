# AtCoder abc151

## Tags:
###### tags: `atcoder`, `abc151`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - Next Alphabet](https://atcoder.jp/contests/abc151/tasks/abc151_a) | Python 3.4.3 | <span style="color:green">AC</span> |   37 bytes |  17 ms | 2940  KB |
| [Problem B - Achieve the Goal](https://atcoder.jp/contests/abc151/tasks/abc151_b) | Python 3.4.3 | <span style="color:green">AC</span> |   235 bytes | 18 ms | 2940 KB |
| [Problem C - Welcome to AtCoder](https://atcoder.jp/contests/abc151/tasks/abc151_c) | Python 3.4.3 | <span style="color:green">AC</span> |   365 bytes | 314 ms | 19620 KB |
| [Problem D - Maze Master](https://atcoder.jp/contests/abc151/tasks/abc151_d) | ? | <span style="color:orange">?</span> | ? bytes | ? ms | ? KB |
| [Problem E - Max-Min Sums](https://atcoder.jp/contests/abc151/tasks/abc151_e) | ? | <span style="color:orange">?</span> | ? bytes | ? ms | ? KB |
| [Problem F - Enclose All](https://atcoder.jp/contests/abc151/tasks/abc151_f) | ? | ? | ? bytes | ? ms | ? KB |


## Solutions
### Problem A - Next Alphabet 
```python
l = input()
print(chr(ord(l)+1))
```

### Problem B - Achieve the Goal 
```python
N, K, M = map(int, input().split())
A = list( map(int, input().split()))

cur = 0
for ai in A:
    cur += ai

an = M*N - cur

if an <= K: 
    if an > 0:
        print(an)
    else:
        print('0')
else:
    print('-1')
```

### Problem C - Welcome to AtCoder
```python
from collections import defaultdict

N, M = map(int, input().split())

ac = set()
wa = defaultdict(int)
ttl_wa = 0

for _ in range(M):
    pi, st = input().split()
    pi = int(pi)

    if st == 'AC':
        if pi not in ac:
            ac.add(pi)
            ttl_wa += wa[pi]
    else: # st == 'WA'
        wa[pi] += 1

print(len(ac), ttl_wa)
```
