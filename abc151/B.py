# B - Achieve the Goal
# https://atcoder.jp/contests/abc151/tasks/abc151_b

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

