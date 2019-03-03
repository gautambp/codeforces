s = input().split()
n = int(s[0])
k = int(s[1])
s = input().split()
cnt = 0
for i in s:
    if int(i)+k <= 5:
        cnt += 1
print(cnt // 3)
