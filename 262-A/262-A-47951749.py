s = input().split()
n = int(s[0])
k = int(s[1])
l = input().split()
cnt = 0
for i in range(n):
    if l[i].count('4') + l[i].count('7') <= k:
        cnt += 1
print(cnt)