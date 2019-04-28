# B - Resale
# https://atcoder.jp/contests/abc125/tasks/abc125_b

N = int(raw_input())

V = map(int, raw_input().split())
C = map(int, raw_input().split())

X_Y = 0

for i in range(N):
    if V[i] - C[i] > 0:
        X_Y += V[i] - C[i]

print '{}'.format(X_Y)
