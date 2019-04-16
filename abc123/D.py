# D - Cake 123
# https://atcoder.jp/contests/abc123/tasks/abc123_d

X, Y, Z, K = map(int, raw_input().split())

A = sorted(map(int,raw_input().split()), reverse=True)
B = sorted(map(int,raw_input().split()), reverse=True)
C = sorted(map(int,raw_input().split()), reverse=True)

AB = sorted([a+b for a in A for b in B], reverse=True)
ABC = sorted([ab + c for ab in AB[:K] for c in C], reverse=True)

for i in ABC[:K]:
    print '{}'.format(i)
