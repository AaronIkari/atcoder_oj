# AtCoder abc124

## Tags:
###### tags: `atcoder`, `abc124`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - Buttons](https://atcoder.jp/contests/abc124/tasks/abc124_a) | Python 2.7 | <span style="color:green">AC</span> |  158 bytes |  11 ms |  2568 KB |
| [Problem B - Great Ocean View](https://atcoder.jp/contests/abc124/tasks/abc124_b) | Python 2.7 | <span style="color:green">AC</span> |  266 bytes |  10 ms | 2568  KB |
| [Problem C - Coloring Colorfully](https://atcoder.jp/contests/abc124/tasks/abc124_c) | Python 2.7 | <span style="color:green">AC</span> | 346  bytes |  32 ms | 2692 KB |
| [Problem D - Handstand](https://atcoder.jp/contests/abc124/tasks/abc124_d) | ? | ? |  ? bytes | ? ms | ? KB |


## Solutions
### Problem A - Buttons
```python
A, B = map(int, raw_input().split())
print '{}'.format( max(A+A-1, max(B+B-1, A+B)) )
```

### Problem B - Great Ocean View

```python
N = int(input())
H = map(int, raw_input().split())
max_h = -1
num_inns = 0

for h in H:
    if h >= max_h:
        num_inns += 1
        max_h = h

print '{}'.format(num_inns)
```

### Problem C - Coloring Colorfully
```python
S = raw_input()

num0 = 0
num1 = 0
beg0 = '0'
beg1 = '1'

for s in S:
    if s != beg0:
        num0 += 1
    else:
        num1 += 1
    beg0 = '0' if beg0 == '1' else '1'
    beg1 = '0' if beg1 == '1' else '1'

print '{}'.format(min(num0, num1))
```
### Problem D - Handstand
<img align="center" src="https://i.imgur.com/pfIF8Ma.png"></img>
