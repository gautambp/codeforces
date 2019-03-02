s = input().split()
k = int(s[0])
r = int(s[1])
cnt = 1
while True:
    if cnt*k % 10 == r or cnt*k % 10 == 0:
        print(cnt)
        break
    cnt += 1