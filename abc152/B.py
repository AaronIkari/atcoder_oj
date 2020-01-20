# B - Comparing Strings
# https://atcoder.jp/contests/abc152/tasks/abc152_b

a, b = map(int, input().split())

ret = [str(a)*b, str(b)*a]
ret.sort()

print(ret[0])
