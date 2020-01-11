# D - Semi Common Multiple
# https://atcoder.jp/contests/abc150/tasks/abc150_d

N, M = map(int, input().split())
A = list(set(map(lambda x : int(x)//2, input().split())))

def _gcd(a, b):
    return a if b == 0 else _gcd(b, a%b)

def _lcm(a,b):
    return (a*b) // _gcd(a,b)

lcm = A[0] 
for ai in A[1:]:
    lcm = _lcm(lcm, ai)

ret = (M//lcm + 1)//2

for ai in A[1:]:
    if (lcm // ai) % 2 == 0:
        ret = 0
        break 

print(ret)
