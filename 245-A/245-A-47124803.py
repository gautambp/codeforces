a_cnt = 0
b_cnt = 0
for _ in range(int(input())):
    (t, x, y) = [int(i) for i in input().strip().split(' ')]
    if t == 1:
        a_cnt += (x-y)
    if t == 2:
        b_cnt += (x-y)

if a_cnt >= 0:
    print('LIVE')
else:
    print('DEAD')
if b_cnt >= 0:
    print('LIVE')
else:
    print('DEAD')