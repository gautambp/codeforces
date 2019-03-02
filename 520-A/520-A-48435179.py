import string

n = int(input())
s = input().lower()
found = True
for ch in string.ascii_lowercase:
    if s.find(ch) == -1:
        found = False
        break
print('YES' if found else 'NO')