# AtCoder abc122

## Tags:
###### tags: `atcoder`, `abc122`

## Overview
| Problems | Language  | Status | Code size | Exec Time | Memory |  
| :--------: | :--------: | :--------: | :--------: | :--------: | :--------: |
| [A - Double Helix](https://atcoder.jp/contests/abc122/tasks/abc122_a) | Python 2.7 | <span style="color:green">AC</span> |  193 bytes |  10ms |  2568 KB |
| [B - ATCoder](https://atcoder.jp/contests/abc122/tasks/abc122_b) | Python 2.7 | <span style="color:green">AC</span> |  448 bytes |  10 ms |  2568 KB |
| [C - GeT AC](https://atcoder.jp/contests/abc122/tasks/abc122_c) | Python 2.7 | <span style="color:green">AC</span> |  392 bytes |  378 ms |  8436 KB |
| [D - We Like AGC](https://atcoder.jp/contests/abc122/tasks/abc122_d) | Python 2.7 | <span style="color:green">AC</span> |  751 bytes |  125 ms |  3332 KB |


## Solutions
### A - Double Helix
```python
bases_dict = {'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
base = raw_input()

print '{}'.format(bases_dict[base])
```

### Problem B - ATCoder

```python
S = raw_input()
num = 0
max_num = 0

for s_id in range(len(S)):
    if S[s_id] == 'A' or S[s_id] == 'T' or S[s_id] == 'C' or S[s_id] == 'G':
        num += 1
    else:
        if num != 0 and max_num < num:
            max_num = num
            num = 0

    if s_id == len(S) - 1 and num != 0 and max_num < num:
        max_num = num

print '{}'.format(max_num)

```

### Problem C - GeT AC
```python
N, Q = map(int, raw_input().split())
S = raw_input()

cnt = [0] * (len(S) + 1)

for s_id in range(len(S)):
    cnt[s_id + 1] = cnt[s_id]
    if S[s_id] == 'C' and S[s_id - 1] == 'A':
        cnt[s_id + 1] += 1

for _ in range(Q):
    l, r = map(int, raw_input().split())
    print '{}'.format(cnt[r] - cnt[l])
```


## Problem D - We Like AGC
```python
N = int(input())
memo = [{} for i in range(N+1)]

MODULO = 10**9 + 7

def legal(prev4):
    for i in range(len(prev4)):
        check = list(prev4)
        if i >= 1:
            check[i], check[i-1] = check[i-1], check[i]
        if ''.join(check).count('AGC') >= 1:
            return False
    return True

def dfs(cur, prev3):

    if prev3 in memo[cur]:
        return memo[cur][prev3]
    if cur == N:
        return 1

    cnt = 0
    for c in 'ACGT':
        prev4 = prev3 + c
        if legal(prev4):
            cnt = (cnt + dfs(cur + 1, prev4[1:])) % MODULO

    memo[cur][prev3] = cnt
    return cnt

print '{}'.format(dfs(0, '___'))
```
