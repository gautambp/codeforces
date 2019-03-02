n = int(input())
s = input().strip()
sf = s.count('SF')
fs = s.count('FS')
if sf > fs:
    print('YES')
else:
    print('NO')
