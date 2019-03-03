l = int(input())
a = int(input())
p = int(input())

cnt = 0
while p >= 4 and a >= 2 and l >= 1:
    p -= 4
    a -= 2
    l -= 1
    cnt += 7
print(cnt)
