N = int(input())
A = list(map(int, raw_input().split()))

def gcd(m,n):
    return m if n == 0 else gcd(n, m%n)

L = [0] * (N+1)
R = [0] * (N+1)

# L: list
# boundary: L[0] = 0, L[N-1] = 0
# L[i]: previous (i-1)-th gcd value, i = [0, ..., N-2]
for i in range(N-1):
    L[i+1] = gcd(L[i], A[i])

# R: list
# boundary: R[0] = 0, R[N-1] = 0
# R[i]: last (N-i)-th gcd value, i = [N-1, ..., 1]
for i in range(N-1, 0, -1):
    R[i] = gcd(R[i+1], A[i])

max_gcd = 0
for i in range(N):
    if gcd(L[i], R[i+1]) > max_gcd:
        max_gcd = gcd(L[i], R[i+1])

print '{}'.format(max_gcd)
