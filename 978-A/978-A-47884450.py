n = int(input())
l = list(map(int, input().split()))
s = ''
d = {}
cnt = 0
for i in range(len(l)-1, -1, -1):
    if l[i] not in d:
        s = str(l[i]) + ' ' + s
        d[l[i]] = i
        cnt += 1
print(cnt)
print(s)
