# B - ATCoder
# https://atcoder.jp/contests/abc122/tasks/abc122_b

S = raw_input()
num = 0
max_num = 0

for s_id in range(len(S)):
    if S[s_id] == 'A' or S[s_id] == 'T' or S[s_id] == 'C' or S[s_id] == 'G':
        num += 1
    else:
        if num != 0 and max_num < num:
            max_num = num
            num = 0

    if s_id == len(S) - 1 and num != 0 and max_num < num:
        max_num = num

print '{}'.format(max_num)
