# C - GeT AC
# https://atcoder.jp/contests/abc122/tasks/abc122_c

N, Q = map(int, raw_input().split())
S = raw_input()

cnt = [0] * (len(S) + 1)

for s_id in range(len(S)):
    cnt[s_id + 1] = cnt[s_id]
    if S[s_id] == 'C' and S[s_id - 1] == 'A':
        cnt[s_id + 1] += 1

for _ in range(Q):
    l, r = map(int, raw_input().split())
    print '{}'.format(cnt[r] - cnt[l])
