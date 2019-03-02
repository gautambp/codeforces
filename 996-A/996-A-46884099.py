n = int(input())
cnt = 0
for i in [100, 20, 10, 5, 1]:
    cnt += int(n/i)
    n = n%i
print(cnt)