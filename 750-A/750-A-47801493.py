s = input().split()
n = int(s[0])
k = int(s[1])
t = 240 - k
cnt = 0
while True:
    t -= (cnt+1)*5
    if t < 0 or cnt+1 > n:
        break
    cnt += 1
    #print('{} {}'.format(t, cnt))

print(cnt)
