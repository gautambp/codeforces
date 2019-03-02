pnos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
s = input().split()
n, m = int(s[0]), int(s[1])
for i in range(len(pnos)):
    if pnos[i] == n:
        break
print('YES' if pnos[i+1] == m else 'NO')