# D - Prediction and Restriction
# https://atcoder.jp/contests/abc149/tasks/abc149_d


N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

def opt(seg):
    # dp[STEP][R/P/S]
    dp = [ [-1, -1, -1] for _ in range(len(seg))]

    dp[0][0] = (R if seg[0] == 's' else 0)
    dp[0][1] = (P if seg[0] == 'r' else 0)
    dp[0][2] = (S if seg[0] == 'p' else 0)

    for i in range(1, len(seg)):
        dp[i][0] = (R if seg[i] == 's' else 0) + max(dp[i-1][1], dp[i-1][2])
        dp[i][1] = (P if seg[i] == 'r' else 0) + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = (S if seg[i] == 'p' else 0) + max(dp[i-1][0], dp[i-1][1])

    return max(dp[-1])

segs = list()

for K_idx in range(K):
    segs.append( T[K_idx::K] )

print('{}'.format(sum(map(opt, segs))))
