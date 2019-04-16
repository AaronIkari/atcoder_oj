# C - Five Transportations
# https://atcoder.jp/contests/abc123/tasks/abc123_c

NUM_TRANSPORTATIONS = 5
N = int(input())

min_t = float("inf")

for t in range(NUM_TRANSPORTATIONS):
    tt = int(input())
    if tt < min_t:
        min_t = tt
        
print '{}'.format( (N-1) / min_t + 5)
