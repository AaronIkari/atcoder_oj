# B - Can you solve this?
# https://atcoder.jp/contests/abc121/tasks/abc121_b

N, M, C = map(int, raw_input().split())
B = list(map(int, raw_input().split()))

num_solve = 0
for _ in range(N):
    A = list(map(int, raw_input().split()))
    D = sum( a*b for (a,b) in zip(A, B)) + C
    if D > 0:
        num_solve += 1

print '{}'.format(num_solve)
