# B - Count ABC
# https://atcoder.jp/contests/abc150/tasks/abc150_b

N = int(input())
S = input()

ret = 0

for i in range(0, N-2):
    if S[i] == 'A' and S[i+1] == 'B' and S[i+2] == 'C':
        ret += 1

print(ret)
