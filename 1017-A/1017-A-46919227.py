n = int(input())
tid = 1
tsum = 0
for idx in range(n):
    s = sum([int(i) for i in input().strip().split(' ')])
    if idx == 0:
        tsum = s
    else:
        if s > tsum:
            tid += 1
print(tid)
