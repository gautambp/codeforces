l = list(map(int, input().split()))
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
if len(d) == 1:
    print(3)
elif len(d) == 2:
    print(2)
elif len(d) == 3:
    print(1)
else:
    print(0)
