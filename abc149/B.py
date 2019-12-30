# B - Greedy Takahashi
# https://atcoder.jp/contests/abc149/tasks/abc149_b

A, B, K = map(int, raw_input().split())

if K >= A+B:
    print '0 0'
elif K >= A:
    K -= A
    print '0 {}'.format(B-K)
else:
    print '{} {}'.format(A-K, B)
