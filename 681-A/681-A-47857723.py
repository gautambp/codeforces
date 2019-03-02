found = False
for _ in range(int(input())):
    s = input().split()
    s1 = int(s[1])
    s2 = int(s[2])
    if s1 >= 2400 and s2 > s1:
        found = True
        
print('YES' if found else 'NO')