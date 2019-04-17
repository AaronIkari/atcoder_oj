# C - Coloring Colorfully
# https://atcoder.jp/contests/abc124/tasks/abc124_c

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
