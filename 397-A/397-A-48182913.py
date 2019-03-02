n = int(input())
l = [None]*n
r = [0]*101
for i in range(n):
    l[i] = list(map(int, input().split()))

for i in range(l[0][0], l[0][1]):
    r[i] = 1

for i in range(1, n):
    il = l[i][0]
    ir = l[i][1]
    for j in range(il, ir):
        r[j] = 0

print(sum(r))