s = input().split()
n = int(s[0])
k = int(s[1])
l = list(map(int, input().split()))
d = {l[i]:i+1 for i in range(n)}
if len(d) >= k:
    print('YES')
    for i in d:
        k -= 1
        print(d[i], end=' ')
        if k <= 0:
            break
else:
    print('NO')