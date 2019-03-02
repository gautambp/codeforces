n = int(input())
s = input().split()
td = {1:[], 2:[], 3:[]}
for i in range(n):
    td[int(s[i])].append(i+1)
t = 99999999999
for k in [1, 2, 3]:
    if len(td[k]) < t:
        t = len(td[k])
print(t)
for i in range(t):
    for k in [1, 2, 3]:
        print(td[k].pop(), end=' ')
    print('')