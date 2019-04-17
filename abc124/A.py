# A - Buttons
# https://atcoder.jp/contests/abc124/tasks/abc124_a

A, B = map(int, raw_input().split())
print '{}'.format( max(A+A-1, max(B+B-1, A+B)) )
