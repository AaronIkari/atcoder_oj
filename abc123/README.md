# AtCoder abc123

## Tags:
###### tags: `atcoder`, `abc123`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :--------: | :--------: | :--------: | :--------: | :--------: | :--------: |
| [A - Five Antennas](https://atcoder.jp/contests/abc123/tasks/abc123_a) | Python 2.7 | <span style="color:green">AC</span> | 262 bytes | 10 ms | 2568 KB |
| [B - Five Dishes](https://atcoder.jp/contests/abc123/tasks/abc123_b) | Python 2.7 | <span style="color:green">AC</span> | 376 bytes | 11 ms | 2568 KB |
| [C - Five Transportation](https://atcoder.jp/contests/abc123/tasks/abc123_c) | Python 2.7 | <span style="color:green">AC</span> | 297 bytes | 10 ms | 2568 KB |
| [D - Cake 123](https://atcoder.jp/contests/abc123/tasks/abc123_d) | Python 2.7 | <span style="color:green">AC</span> | 461 bytes | 1655 ms | 163648 KB |


## Solutions
### Problem A - Five Antenna
```python
NUM_ANTENNAS = 5

antennas = list()
for _ in range(NUM_ANTENNAS):
    antennas.append(int(raw_input()))

k = int(raw_input())

print 'Yay!' if (antennas[-1]-antennas[0]) <= k else ':('
```

### Problem B - Five Dishes

```python
NUM_DISHES = 5
tt = 0
itvs = list()

for i in range(NUM_DISHES):
    st = int(raw_input())
    tt += st
    if st % 10 == 0:
        itvs.append(0)
    else:
        itvs.append(10 - st % 10)

itvs.sort()

for interval in range(len(itvs) - 1):
    tt += itvs[interval]

print "{}".format(tt)
```

### Problem C - Five Transportation
```python
NUM_TRANSPORTATIONS = 5

N = int(input())
min_t = float("inf")

for t in range(NUM_TRANSPORTATIONS):
    tt = int(input())
    if tt < min_t:
        min_t = tt

print '{}'.format( (N-1) / min_t + 5)
```


### Problem D - Cake 123
```python
X, Y, Z, K = map(int, raw_input().split())

A = sorted(map(int,raw_input().split()), reverse=True)
B = sorted(map(int,raw_input().split()), reverse=True)
C = sorted(map(int,raw_input().split()), reverse=True)

AB = sorted([a+b for a in A for b in B], reverse=True)
ABC = sorted([ab + c for ab in AB[:K] for c in C], reverse=True)

for i in ABC[:K]:
    print '{}'.format(i)
```
