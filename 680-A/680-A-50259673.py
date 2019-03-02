from collections import defaultdict
l = list(map(int, input().split()))
d = defaultdict(int)
t = sum(l)
for li in l:
    d[li] += 1
s3 = s2 = None
for k in d:
    if d[k] >= 3:
        s3 = 3*k
    elif d[k] == 2:
        s2 = (2*k if s2 == None or s2 < 2*k else s2)
if s2 != None and s3 != None:
    t -= (s2 if s2 > s3 else s3)
elif s2 != None:
    t -= s2
elif s3 != None:
    t -= s3
print(t)