from collections import defaultdict

n = int(input())
s = input()
d = defaultdict(int)
for i in range(n-1):
    d[s[i]+s[i+1]] += 1
max_val = 0
max_str = ''
for k in d:
    if d[k] > max_val: 
        max_val = d[k]
        max_str = k
print(max_str)