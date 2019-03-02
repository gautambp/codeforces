n = int(input())
m = int(input())
l = []
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
for i in range(n):
    m -= l[i]
    if m <= 0:
        break
print(i+1)