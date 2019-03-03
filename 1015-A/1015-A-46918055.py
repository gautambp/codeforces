(n, m) = [int(i) for i in input().strip().split(' ')]
all_pts = {}
for i in range(m):
    all_pts[i+1] = i+1
for i in range(n):
    (l, r) = [int(i) for i in input().strip().split(' ')]
    for j in range(l, r+1):
        if j in all_pts:
            del all_pts[j]
if len(all_pts) == 0:
    print(0)
else:
    print(len(all_pts))
    for i in all_pts:
        print(all_pts[i], end=' ')
print('')
