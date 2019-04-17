# C - Energy Drink Collector
# https://atcoder.jp/contests/abc121/tasks/abc121_c

N, M = map(int, raw_input().split())

stores = list()
for _ in range(N):
    stores.append( tuple(map(int, raw_input().split())) )

stores.sort(key=lambda x : x[0])

money = 0
cans_cnt = 0
for cost_i, cans_i in stores:
    buy_i = min(M - cans_cnt, cans_i)
    money += (cost_i * buy_i)
    cans_cnt += buy_i
    if (cans_cnt == M):
        break

print '{}'.format(money)
