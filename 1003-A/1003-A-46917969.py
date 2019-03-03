n = int(input())
a = [int(i) for i in input().strip().split(' ')]
total = 0
for i in range(n):
    c = a.count(a[i])
    if c > total:
        total = c
print(total)
