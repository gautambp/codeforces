from collections import deque

s = input().split()
n = int(s[0])
m = int(s[1])
a = list(map(int, input().split()))

result = ['0']*m
d = {}
for i in range(m):
    c = None
    if a[i] in d:
        c = d[a[i]]
    else:
        c = deque()
        d[a[i]] = c
    c.append(i)

while True:
    found = True
    max_p = 0
    for i in range(1, n+1):
        if i not in d or len(d[i]) == 0:
            found = False
            break
        p = d[i].popleft()
        if p > max_p:
            max_p = p
    if found == False:
        break
    result[max_p] = '1'
    
print(''.join(result))
