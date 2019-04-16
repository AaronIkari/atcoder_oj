# A - Five Antennas
# https://atcoder.jp/contests/abc123/tasks/abc123_a

NUM_ANTENNAS = 5
antennas = list()
for _ in range(NUM_ANTENNAS):
    antennas.append(int(raw_input()))
k = int(raw_input())
print 'Yay!' if (antennas[-1]-antennas[0]) <= k else ':('
