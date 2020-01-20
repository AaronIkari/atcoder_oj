# C - Low Elements
# https://atcoder.jp/contests/abc152/tasks/abc152_c

N = int(input())
P = list(map(int, input().split()))
 
cur_min = P[0]
ret = 1
for i in range(1, N):
  if P[i] < cur_min:
    cur_min = P[i]
    ret += 1
 
print(ret)
