n = int(input())
l = list(map(int, input().split()))
e = sum(l)
m = max(l)
a = 0
while e>=a:
    a = 0
    for i in range(n):
        a += m-l[i]
    m += 1
print(m-1)
