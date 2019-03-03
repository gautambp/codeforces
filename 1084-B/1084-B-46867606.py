import math

(ns, ss) = '3 4'.strip().split(' ')
(ns, ss) = input().strip().split(' ')
n = int(ns)
s = int(ss)
vstr = '5 3 4'.strip().split(' ')
vstr = input().strip().split(' ')
v = list(map(int, vstr))
min_v = min(v)
for i in range(n):
    if v[i] > min_v:
        s -= (v[i]-min_v)
        v[i] -= (v[i]-min_v)
    if s <= 0:
        break
if s <= 0:
    print(min_v)
else:
    if n*min_v < s:
        print(-1)
    else:
        print(min_v - math.ceil(s/n))
    
