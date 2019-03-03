(n, h) = [int(i) for i in input().strip().split(' ')]
a = list(map(int, input().strip().split(' ')))
cnt = 0
for i in a:
    if i > h: 
        cnt += 2
    else: 
        cnt += 1
print(cnt)
