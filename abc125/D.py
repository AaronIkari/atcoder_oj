# D - Flipping Signs
# https://atcoder.jp/contests/abc125/tasks/abc125_d

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
