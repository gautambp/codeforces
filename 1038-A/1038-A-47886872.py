import string

s = input().split()
n = int(s[0])
k = int(s[1])
s = input()
min_occ = n
found_all = True
for i in range(k):
    cnt = s.count(string.ascii_uppercase[i])
    if cnt == 0:
        found_all = False
        break
    if cnt < min_occ:
        min_occ = cnt

if not found_all:
    print(0)
else:
    print(k*min_occ)
