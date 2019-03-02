s = input().split()
n = int(s[0])
k = int(s[1])
l = list(map(int, input().split()))
cnt = 0
while len(l) > 0 and l[0] <= k:
    cnt += 1
    l.pop(0)
while len(l) > 0 and l[len(l)-1] <= k:
    cnt += 1
    l.pop()
print(cnt)