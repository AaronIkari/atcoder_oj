# C - Count Order
# https://atcoder.jp/contests/abc150/tasks/abc150_c

from itertools import permutations 

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

perm = list(permutations([i+1 for i in range(N)]))

print(abs(perm.index(P) - perm.index(Q)))
