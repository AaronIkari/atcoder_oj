# A - White Cells
# https://atcoder.jp/contests/abc121/tasks/abc121_a

H, W = map(int, raw_input().split())
h, w = map(int, raw_input().split())

print '{}'.format(H*W - (h*W + H*w - h*w))
