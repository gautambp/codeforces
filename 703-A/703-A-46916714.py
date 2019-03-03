n = int(input())
mwin = 0
for _ in range(n):
    (m, c) = [int(i) for i in input().strip().split(' ')]
    if m > c:
        mwin += 1
    elif m < c:
        mwin -= 1
if mwin > 0:
    print('Mishka')
elif mwin < 0:
    print('Chris')
else:
    print('Friendship is magic!^^')
