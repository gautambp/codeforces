n = int(input())
a = list(map(int, input().split()))
s = sum(a)
cnt = 0
for i in range(n):
    if (s-a[i])%2 == 0:
        cnt += 1
print(cnt)