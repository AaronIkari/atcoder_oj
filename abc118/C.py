# C - Monsters Battle Royale
# https://atcoder.jp/contests/abc118/tasks/abc118_c

N = int(input())
A = set(map(int, raw_input().split()))

while len(A) != 1:

    # minimum number of A
    minA = min(A)

    # next round A
    nA = set()
    nA.add(minA)

    for Ai in A:
        if Ai == minA: continue
        if Ai % minA != 0:
            nA.add(Ai%minA)

    # update for next round
    A = nA

print '{}'.format( list(A)[-1])
