# C - Unification
# https://atcoder.jp/contests/abc120/tasks/abc120_c
S = raw_input()

num1 = 0
num0 = 0

for s in S:
    if s == '1':
        num1 += 1
    else:
        num0 += 1

print '{}'.format(2*min(num0, num1))
