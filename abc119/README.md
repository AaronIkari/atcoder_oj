# AtCoder abc119

## Tags:
###### tags: `atcoder`, `abc119`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :-------- | :--------: | :--------: | :--------: | :--------: | :--------: |
| [Problem A - Still TBD](https://atcoder.jp/contests/abc119/tasks/abc119_a) | Python 2.7 | <span style="color:green">AC</span> |  240 bytes |  10 ms |  2568 KB |
| [Problem B - Digital Gifts](https://atcoder.jp/contests/abc119/tasks/abc119_b) | Python 2.7 | <span style="color:green">AC</span> |  346 bytes |  11 ms |  19564 KB |
| [Problem C - Synthetic Kadomatsu](https://atcoder.jp/contests/abc119/tasks/abc119_c) | ? | ? |  ? bytes |  ? ms |  ? KB |
| [Problem D - Lazy Faith](https://atcoder.jp/contests/abc119/tasks/abc119_d) | ? | ? |  ? bytes |  ? ms |  ? KB |


## Solutions
### Problem A - Still TBD
```python
# threshold
TY, TM, TD = 2019, 4, 30

Y, M, D = map(int, raw_input().split('/'))

if M > 4:
    print '{}'.format('TBD')
else:
    print '{}'.format('Heisei')
```

### Problem B - Foods Loved by Everyone 
```python
ER = 380000.0

N = int(input())

total_yens = 0.0

for i in range(N):
    u_i, x_i = raw_input().split()
    if x_i == 'JPY':
        total_yens += int(u_i)
    else: # x_i == 'BTC'
        total_yens += (float(u_i) * ER)

print '{0:.4f}'.format(total_yens)
```
