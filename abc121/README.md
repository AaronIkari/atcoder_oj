# AtCoder abc121

## Tags:
###### tags: `atcoder`, `abc122`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - White Cells](https://atcoder.jp/contests/abc121/tasks/abc121_a) | Python 2.7 | <span style="color:green">AC</span> |  196 bytes |  10 ms |  2568 KB |
| [Problem B - Can you solve this?](https://atcoder.jp/contests/abc121/tasks/abc121_b) | Python 2.7 | <span style="color:green">AC</span> |  363 bytes |  10 ms |  2568 KB |
| [Problem C - Energy Drink Collector](https://atcoder.jp/contests/abc121/tasks/abc121_c) | Python 2.7 | <span style="color:green">AC</span> |  495 bytes |  398 ms |  21236 KB |
| [Problem D - XOR World](https://atcoder.jp/contests/abc121/tasks/abc121_d) | Python 2.7 | <span style="color:gray"> ? </span> |  <span style="color:gray"> ? </span> bytes | <span style="color:gray"> ? </span> ms | <span style="color:gray"> ? </span> KB |


## Solutions
### Problem A - White Cells
```python
H, W = map(int, raw_input().split())
h, w = map(int, raw_input().split())

print '{}'.format(H*W - (h*W + H*w - h*w))
```

### Problem B - Can you solve this?

```python
N, M, C = map(int, raw_input().split())
B = list(map(int, raw_input().split()))

num_solve = 0
for _ in range(N):
    A = list(map(int, raw_input().split()))
    D = sum( a*b for (a,b) in zip(A, B)) + C
    if D > 0:
        num_solve += 1

print '{}'.format(num_solve)
```

### Problem C - Energy Drink Collector
```python
N, M = map(int, raw_input().split())

stores = list()
for _ in range(N):
    stores.append( tuple(map(int, raw_input().split())) )

stores.sort(key=lambda x : x[0])

money = 0
cans_cnt = 0
for cost_i, cans_i in stores:
    buy_i = min(M - cans_cnt, cans_i)
    money += (cost_i * buy_i)
    cans_cnt += buy_i
    if (cans_cnt == M):
        break

print '{}'.format(money)
```
### Problem D - XOR World
<img align="center" src="https://i.imgur.com/pfIF8Ma.png"></img>
