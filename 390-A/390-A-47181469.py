hor_l = set()
ver_l = set()
for _ in range(int(input())):
    (x, y) = [int(i) for i in input().split(' ')]
    hor_l.add(x)
    ver_l.add(y)
l = len(hor_l)
if len(ver_l) < l:
    l = len(ver_l)
print(l)