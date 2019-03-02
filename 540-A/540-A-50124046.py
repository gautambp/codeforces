n = int(input())
src = input()
tgt = input()
cnt = 0
for i in range(n):
    d = abs(int(tgt[i]) - int(src[i]))
    if d > 5: d = 10-d
    cnt += d
print(cnt)