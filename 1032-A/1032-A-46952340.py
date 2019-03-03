import math

(n, k) = [int(i) for i in input().strip().split(' ')]
a = [int(i) for i in input().strip().split(' ')]
u_set = {}
max_cnt = 0
for i in a:
    u_set[i] = i
    cnt = a.count(i)
    if cnt > max_cnt: max_cnt = cnt
s_u = len(u_set)
d = math.ceil(max_cnt/k)
print(k*d*s_u - n)
