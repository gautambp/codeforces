import math

n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))
if x > y:
    print(len(a))
else:
    cnt = sum(list(1 for i in a if i <= x))
    print(math.ceil(cnt/2))
