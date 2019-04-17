# D - We Like AGC
# https://atcoder.jp/contests/abc122/tasks/abc122_d
# https://img.atcoder.jp/abc122/editorial.pdf

N = int(input())
memo = [{} for i in range(N+1)]

MODULO = 10**9 + 7

def legal(prev4):
    for i in range(len(prev4)):
        check = list(prev4)
        if i >= 1:
            check[i], check[i-1] = check[i-1], check[i]
        if ''.join(check).count('AGC') >= 1:
            return False
    return True

def dfs(cur, prev3):

    if prev3 in memo[cur]:
        return memo[cur][prev3]
    if cur == N:
        return 1

    cnt = 0
    for c in 'ACGT':
        prev4 = prev3 + c
        if legal(prev4):
            cnt = (cnt + dfs(cur + 1, prev4[1:])) % MODULO

    memo[cur][prev3] = cnt
    return cnt

print '{}'.format(dfs(0, '___'))
