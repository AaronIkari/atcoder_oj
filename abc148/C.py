# C - Snack
# https://atcoder.jp/contests/abc148/tasks/abc148_c

def gcd(A, B):
    if B > A: 
        A, B = B, A

    if B == 0:
        return A
    else:
        return gcd(B, A%B)


A, B = map(int, raw_input().split())

gcdAB = gcd(A, B)

print '{}'.format(A*B/gcdAB)

