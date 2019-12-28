# E - Double Factorial
# https://atcoder.jp/contests/abc148/tasks/abc148_e

N = int(input())

ret = 0

if N % 2 == 0:
    N //= 2
    while N > 0:
        N //= 5
        ret += N

print '{}'.format(ret)
        
