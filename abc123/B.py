# Five Dishes
# https://atcoder.jp/contests/abc123/tasks/abc123_b

NUM_DISHES = 5
tt = 0
itvs = list()

for i in range(NUM_DISHES):
    st = int(raw_input())
    tt += st
    if st % 10 == 0:
        itvs.append(0)
    else:
        itvs.append(10 - st % 10)

itvs.sort()

for interval in range(len(itvs) - 1):
    tt += itvs[interval]

print "{}".format(tt)
