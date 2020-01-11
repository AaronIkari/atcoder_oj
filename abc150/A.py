# A - 500 Yen Coins
# https://atcoder.jp/contests/abc150/tasks/abc150_a

K, X = map(int, input().split())

if 500 * K >= X:
    print('Yes')
else:
    print('No')
