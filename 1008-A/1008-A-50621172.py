vl = ['a', 'e', 'i', 'o', 'u']
s = input()
r = True
for i in range(len(s)-1):
    if s[i] not in vl:
        if s[i] != 'n' and s[i+1] not in vl:
            r = False
            break
if s[len(s)-1] != 'n' and s[len(s)-1] not in vl:
    r = False
print('YES' if r else 'NO')
