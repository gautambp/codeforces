n = int(input())
s = input().split()
d = {}
for i in range(1, n+1):
    d[i] = int(s[i-1])

found = False
for i in range(1, n+1):
    if d[d[d[i]]] == i:
        found = True
        break
print('YES' if found else 'NO')