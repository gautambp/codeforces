n = int(input())
cs = 0
capacity = 0
for _ in range(n):
    a,b = list(map(int, input().split()))
    cs -= a
    cs += b
    if cs > capacity:
        capacity = cs
print(capacity)