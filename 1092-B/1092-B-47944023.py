n = int(input())
l = list(map(int, input().split()))
l.sort()
cnt = 0
for i in range(1, n, 2):
    if l[i] != l[i-1]:
        cnt += l[i]-l[i-1]
print(cnt)
