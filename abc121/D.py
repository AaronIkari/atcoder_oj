# D - XOR World
# https://atcoder.jp/contests/abc121/tasks/abc121_d

def two2ten(two):
    base = 1
    ten = 0
    for i in two:
        ten += i*base
        base *= 2
    return ten

def ten2two(ten):
    two = list()
    while ten > 0:
        two.append(ten%2)
        ten /= 2
    return two

def find_first_1(two):
    for two_id in range(len(two)):
        if two[two_id] == 1:
            return two_id

A, B = map(int, raw_input().split())
b = ten2two(B)
pos1 = find_first_1(b)
ret = [0]*len(b)
t = B - A + 1

while t > 0:
    for b_id in range(len(b)):
        ret[b_id] += b[b_id]

    b[pos1] = 0
    for b_id in range(0, pos1):
        b[b_id] = 1

    pos1 = find_first_1(b)
    t -= 1

for ret_id in range(len(ret)):
    ret[ret_id] %= 2

print '{}'.format(two2ten(ret))
