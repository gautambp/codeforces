from collections import defaultdict

s = input().split()
n, k = int(s[0]), int(s[1])
s = input()
d = defaultdict(int)
success = True
for i in range(n):
    d[s[i]] += 1
    if d[s[i]] > k:
        success = False
        break
print('YES' if success else 'NO')