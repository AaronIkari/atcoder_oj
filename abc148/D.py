# D - Brick Break
# https://atcoder.jp/contests/abc148/tasks/abc148_d

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
