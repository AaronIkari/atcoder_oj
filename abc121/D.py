# D - XOR World
# https://atcoder.jp/contests/abc121/tasks/abc121_d


def xor_from0(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    else: # n % 4 == 3
        return 0

A, B = map(int, raw_input().split())
print '{}'.format(xor_from0(A-1) ^ xor_from0(B))
