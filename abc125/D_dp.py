# D - Flipping Signs
# https://atcoder.jp/contests/abc125/tasks/abc125_

import sys
sys.setrecursionlimit(1000000)

N = int(input())
A = list( map(int, raw_input().split()) )

rcd = dict()

# dynamic programming, dp(current_position, (i-1)-th_sign)
def dp(pos, sign):

    # boundary condition
    if pos == N-1:
        if sign == 0:
            return A[pos]
        else:
            return -A[pos]

    # if visit (pos, sign) state before
    if (pos, sign) in rcd:
        return rcd[(pos, sign)]

    elif sign == 0:
        # memorize
        rcd[(pos, sign)] = max( dp(pos+1, 0) + A[pos], dp(pos+1, 1) - A[pos])
        return rcd[(pos, sign)]

    else: # st == 1
        # memorize
        rcd[(pos, sign)] = max( dp(pos+1, 0) -  A[pos], dp(pos + 1, 1) + A[pos])
        return rcd[(pos, sign)]

print '{}'.format( dp(0,0) )
