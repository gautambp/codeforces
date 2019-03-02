s = input().split()
n, x = int(s[0]), int(s[1])
s = input().split()
s_sum = 0
for i in range(n):
    s_sum += int(s[i])
cnt = abs(s_sum)
print(cnt//x if cnt%x == 0 else 1+cnt//x)