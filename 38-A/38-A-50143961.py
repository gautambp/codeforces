n = input()
d = list(map(int, input().split()))
s = input().split()
a, b = int(s[0]), int(s[1])
cnt = 0
for i in range(a, b):
    cnt += d[i-1]
print(cnt)