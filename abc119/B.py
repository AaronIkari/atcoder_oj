# B - Digital Gifts
# https://atcoder.jp/contests/abc119/tasks/abc119_b
ER = 380000.0

N = int(input())

total_yens = 0.0

for i in range(N):
    u_i, x_i = raw_input().split()
    if x_i == 'JPY':
        total_yens += int(u_i)
    else: # x_i == 'BTC'
        total_yens += (float(u_i) * ER)

print '{0:.4f}'.format(total_yens)
