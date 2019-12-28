# B - Strings with the Same Length
# https://atcoder.jp/contests/abc148/tasks/abc148_b

N = int(input())
S, T = raw_input().split()

ret = ''

for n in range(N):
    ret += S[n]
    ret += T[n]

print '{}'.format(ret)
