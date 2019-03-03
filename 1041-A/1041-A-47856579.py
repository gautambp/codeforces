n = int(input())
l = list(map(int, input().split()))
m = 0
l.sort()
for i in range(1, n):
    if l[i] - l[i-1] != 1:
        m += l[i]-l[i-1]-1
print(m)
