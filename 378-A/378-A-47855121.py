def findWinner(a, b, n):
    if abs(a-n) > abs(b-n): return 1
    if abs(a-n) < abs(b-n): return -1
    return 0

s = input().split()
a = int(s[0])
b = int(s[1])

a_win = 0
b_win = 0
draw = 0

for i in range(1, 7):
    w = findWinner(a, b, i)
    if w == 1: b_win += 1
    if w == -1: a_win += 1
    if w == 0: draw += 1
print('{} {} {}'.format(a_win, draw, b_win))