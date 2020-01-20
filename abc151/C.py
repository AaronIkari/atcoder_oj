# C - Welcome to AtCoder
# https://atcoder.jp/contests/abc151/tasks/abc151_c

from collections import defaultdict

N, M = map(int, input().split())

ac = set()
wa = defaultdict(int)
ttl_wa = 0

for _ in range(M):
    pi, st = input().split()
    pi = int(pi)

    if st == 'AC':
        if pi not in ac:
            ac.add(pi)
            ttl_wa += wa[pi]
    else: # st == 'WA'
        wa[pi] += 1

print(len(ac), ttl_wa)
