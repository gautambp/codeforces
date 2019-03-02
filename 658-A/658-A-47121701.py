(n, c) = [int(i) for i in input().strip().split(' ')]
p = [int(i) for i in input().strip().split(' ')]
t = [int(i) for i in input().strip().split(' ')]

l_pts = 0
r_pts = 0
l_cnt = 0
r_cnt = 0
for i in range(n):
    l_cnt += t[i]
    if p[i] - (l_cnt*c) > 0:
        l_pts += p[i] - (l_cnt*c)
    r_cnt += t[n-i-1]
    if p[n-i-1] - (r_cnt*c) > 0:
        r_pts += p[n-i-1] - (r_cnt*c)
if l_pts > r_pts:
    print('Limak')
elif r_pts > l_pts:
    print('Radewoosh')
else:
    print('Tie')